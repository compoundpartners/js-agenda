# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-23 03:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import djangocms_text_ckeditor.fields
import js_color_picker.fields
import sortedm2m.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0020_old_tree_cleanup'),
        ('js_events', '0013_event_redirect_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='js_agenda_agenda', serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Title')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='js_agenda_session', serialize=False, to='cms.CMSPlugin')),
                ('start_time', models.CharField(max_length=255, verbose_name='Start Time')),
                ('end_time', models.CharField(max_length=255, verbose_name='End Time')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('session_type', models.CharField(blank=True, max_length=255, verbose_name='Type')),
                ('description', djangocms_text_ckeditor.fields.HTMLField(blank=True, default='', verbose_name='Description')),
                ('speakers_list_title', models.CharField(blank=True, max_length=255, verbose_name='Speakers List Title Type 1')),
                ('speakers_list_title2', models.CharField(blank=True, max_length=255, verbose_name='Speakers List Title Type 2')),
                ('backgrond_color', js_color_picker.fields.RGBColorField(blank=True, colors={'#0067A5': 'Dark Blue', '#009fe3': 'Blue', '#0A80C7': 'Medium Blue', '#2D9CDE': 'Light Blue', '#34BCE1': 'Sky', '#545454': 'Dark Grey', '#68C0B5': 'Teal', '#69CCE7': 'Light Sky', '#6d6d6d': 'Grey', '#8FD1E9': 'Very Light Sky', '#96D0C9': 'Light Teal', '#999': 'Light Grey', '#9B8DA5': 'Purple', '#B8AEBF': 'Light Purple', '#BBE9E4': 'Very Light Teal', '#C6BDCB': 'Very Light Purple', '#F2F2F2': 'Very Light Grey', '#F8EB91': 'Yellow', '#FEF4B4': 'Light Yellow', '#FF0000': 'White'}, mode='both', null=True, verbose_name='Backgrond color')),
                ('speakers_list', sortedm2m.fields.SortedManyToManyField(blank=True, help_text=None, related_name='sessions', to='js_events.Speaker', verbose_name='Speakers Type 1')),
                ('speakers_list2', sortedm2m.fields.SortedManyToManyField(blank=True, help_text=None, related_name='sessions2', to='js_events.Speaker', verbose_name='Speakers Type 2')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]