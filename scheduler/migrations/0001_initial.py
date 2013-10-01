# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Pilot'
        db.create_table(u'scheduler_pilot', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=55)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=55)),
        ))
        db.send_create_signal(u'scheduler', ['Pilot'])

        # Adding model 'Appointment'
        db.create_table(u'scheduler_appointment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=55)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=55)),
            ('date_of_departure', self.gf('django.db.models.fields.DateField')()),
            ('time_of_departure', self.gf('django.db.models.fields.TimeField')()),
            ('pilot', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scheduler.Pilot'])),
            ('booked_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'scheduler', ['Appointment'])


    def backwards(self, orm):
        # Deleting model 'Pilot'
        db.delete_table(u'scheduler_pilot')

        # Deleting model 'Appointment'
        db.delete_table(u'scheduler_appointment')


    models = {
        u'scheduler.appointment': {
            'Meta': {'object_name': 'Appointment'},
            'booked_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_of_departure': ('django.db.models.fields.DateField', [], {}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '55'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '55'}),
            'pilot': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['scheduler.Pilot']"}),
            'time_of_departure': ('django.db.models.fields.TimeField', [], {})
        },
        u'scheduler.pilot': {
            'Meta': {'object_name': 'Pilot'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '55'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '55'})
        }
    }

    complete_apps = ['scheduler']