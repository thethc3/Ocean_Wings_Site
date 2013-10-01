# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Appointment.aircraft'
        db.add_column(u'scheduler_appointment', 'aircraft',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['scheduler.Aircraft']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Appointment.aircraft'
        db.delete_column(u'scheduler_appointment', 'aircraft_id')


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
            'aircraft': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['scheduler.Aircraft']"}),
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