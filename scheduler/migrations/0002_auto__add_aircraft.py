# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Aircraft'
        db.create_table(u'scheduler_aircraft', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('short_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('tail_number', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('hours_before_inspection', self.gf('django.db.models.fields.IntegerField')()),
            ('cruise_speed', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'scheduler', ['Aircraft'])


    def backwards(self, orm):
        # Deleting model 'Aircraft'
        db.delete_table(u'scheduler_aircraft')


    models = {
        u'scheduler.aircraft': {
            'Meta': {'object_name': 'Aircraft'},
            'cruise_speed': ('django.db.models.fields.IntegerField', [], {}),
            'hours_before_inspection': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'tail_number': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
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