# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from sortedm2m_filter_horizontal_widget.forms import SortedFilteredSelectMultiple
from . import models


@plugin_pool.register_plugin
class AgendaPlugin(CMSPluginBase):
    model = models.Agenda
    name = _('Agenda')
    admin_preview = False
    render_template = 'js_agenda/agenda.html'
    allow_children = True
    child_classes = ['SessionPlugin']

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder': placeholder,
        })
        return context


@plugin_pool.register_plugin
class SessionPlugin(CMSPluginBase):
    model = models.Session
    name = _('Session')
    admin_preview = False
    render_template = 'js_agenda/session.html'
    parent_classes = ['AgendaPlugin']

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder': placeholder,
        })
        return context

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        if db_field.name in ['speakers_list', 'speakers_list2']:
            kwargs['widget'] = SortedFilteredSelectMultiple()
        return super(SessionPlugin, self).formfield_for_manytomany(db_field, request, **kwargs)
