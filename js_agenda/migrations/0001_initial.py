# Regenerated for the v6 branch (django CMS 6 / Django 5.2).
#
# The original 0001_initial depended on ('js_events', '0013_event_redirect_url')
# and created the two speaker relations against js_events.Speaker. js-events is
# the legacy pre-jumpsuite events package and is not installed on this stack, so
# that dependency could not be resolved at all -- migrate raised NodeNotFoundError
# before any table was created. The relations now point at people.Person, which
# is the model jumpsuite-events uses for the equivalent EventContent.hosts.
#
# This replaces 0001_initial rather than adding 0002, because there is no
# deployment of this branch with js_agenda tables to migrate forward from. Sites
# still on master keep their own history; do not merge the two migration
# directories without a squash.

import django.db.models.deletion
import djangocms_text.fields
import js_color_picker.fields
import sortedm2m.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    # __first__ rather than a pinned migration name: CMSPlugin and Person are
    # both created in their app's first migration, and pinning the latest (as
    # makemigrations proposes) would tie this package to one django CMS and one
    # jumpsuite-people release.
    dependencies = [
        ('cms', '__first__'),
        ('people', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='%(app_label)s_%(class)s', serialize=False, to='cms.cmsplugin')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Title')),
            ],
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='%(app_label)s_%(class)s', serialize=False, to='cms.cmsplugin')),
                ('start_time', models.CharField(max_length=255, verbose_name='Start Time')),
                ('end_time', models.CharField(max_length=255, verbose_name='End Time')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('session_type', models.CharField(blank=True, max_length=255, verbose_name='Type')),
                ('description', djangocms_text.fields.HTMLField(blank=True, default='', verbose_name='Description')),
                ('speakers_list_title', models.CharField(blank=True, max_length=255, verbose_name='Speakers List Title Type 1')),
                ('speakers_list_title2', models.CharField(blank=True, max_length=255, verbose_name='Speakers List Title Type 2')),
                ('backgrond_color', js_color_picker.fields.RGBColorField(blank=True, null=True, verbose_name='Backgrond color')),
                ('speakers_list', sortedm2m.fields.SortedManyToManyField(blank=True, help_text=None, related_name='sessions', to='people.person', verbose_name='Speakers Type 1')),
                ('speakers_list2', sortedm2m.fields.SortedManyToManyField(blank=True, help_text=None, related_name='sessions2', to='people.person', verbose_name='Speakers Type 2')),
            ],
            bases=('cms.cmsplugin',),
        ),
    ]
