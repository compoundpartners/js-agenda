# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from cms.models.pluginmodel import CMSPlugin
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from djangocms_text_ckeditor.fields import HTMLField
from sortedm2m.fields import SortedManyToManyField
from js_color_picker.fields import RGBColorField


@python_2_unicode_compatible
class Agenda(CMSPlugin):
    title = models.CharField(
        max_length=255,
        verbose_name=_('Title'),
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title or str(self.pk)


@python_2_unicode_compatible
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
        'js_events.Speaker',
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
        'js_events.Speaker',
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

    def copy_relations(self, oldinstance):
        self.speakers_list = oldinstance.speakers_list.all()
        self.speakers_list2 = oldinstance.speakers_list2.all()
