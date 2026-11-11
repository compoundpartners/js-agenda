# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from cms.models.pluginmodel import CMSPlugin
from django.db import models
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _
from djangocms_text.fields import HTMLField
from sortedm2m.fields import SortedManyToManyField
from js_color_picker.fields import RGBColorField
from people.models import PersonContent


class Agenda(CMSPlugin):
    title = models.CharField(
        max_length=255,
        verbose_name=_('Title'),
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title or str(self.pk)


class Session(CMSPlugin):
    start_time = models.CharField(
        max_length=255,
        verbose_name=_('Start Time'),
    )
    end_time = models.CharField(
        max_length=255,
        verbose_name=_('End Time'),
    )
    title = models.CharField(
        max_length=255,
        verbose_name=_('Title'),
    )
    session_type = models.CharField(
        max_length=255,
        verbose_name=_('Type'),
        blank=True
    )
    description = HTMLField(
        verbose_name=_('Description'),
        default='',
        blank=True
    )
    speakers_list_title = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_('Speakers List Title Type 1')
    )
    speakers_list = SortedManyToManyField(
        'people.Person',
        verbose_name=_('Speakers Type 1'),
        blank=True,
        related_name='sessions',
    )
    speakers_list_title2 = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_('Speakers List Title Type 2')
    )
    speakers_list2 = SortedManyToManyField(
        'people.Person',
        verbose_name=_('Speakers Type 2'),
        blank=True,
        related_name='sessions2',
    )
    backgrond_color = RGBColorField(
        verbose_name=_('Backgrond color'),
        blank=True,
        null=True,
    )
    def __str__(self):
        return self.title or str(self.pk)

    def _speakers_content(self, people):
        """Translated PersonContent for a set of Person groupers, in order.

        The m2m points at the grouper (people.Person), but everything worth
        displaying -- name, role -- lives on PersonContent, one row per
        language. This mirrors EventContent.get_hosts_content in
        jumpsuite-events, which resolves its `hosts` the same way.
        """
        return PersonContent.objects.get_sorted_translations(people, self.language)

    @cached_property
    def speakers_content(self):
        return self._speakers_content(self.speakers_list.all())

    @cached_property
    def speakers_content2(self):
        return self._speakers_content(self.speakers_list2.all())

    def copy_relations(self, oldinstance):
        self.speakers_list.set(oldinstance.speakers_list.all())
        self.speakers_list2.set(oldinstance.speakers_list2.all())
