# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Kunde'
        db.create_table('db_kunde', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nr', self.gf('django.db.models.fields.IntegerField')()),
            ('matchcode', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('anrede', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('firma', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('nachname', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('vorname', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('plz', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('ort', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('strasse', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('telefon', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('mobil', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=254)),
        ))
        db.send_create_signal('db', ['Kunde'])

        # Adding model 'Projects'
        db.create_table('db_projects', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nr', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('kunde', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['db.Kunde'], on_delete=models.PROTECT)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('beschreibung', self.gf('django.db.models.fields.TextField')()),
            ('begin', self.gf('django.db.models.fields.DateField')(null=True)),
            ('ende', self.gf('django.db.models.fields.DateField')(null=True)),
        ))
        db.send_create_signal('db', ['Projects'])


    def backwards(self, orm):
        # Deleting model 'Kunde'
        db.delete_table('db_kunde')

        # Deleting model 'Projects'
        db.delete_table('db_projects')


    models = {
        'db.kunde': {
            'Meta': {'object_name': 'Kunde'},
            'anrede': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'firma': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'matchcode': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'mobil': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'nachname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nr': ('django.db.models.fields.IntegerField', [], {}),
            'ort': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'plz': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'strasse': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'telefon': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'vorname': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'db.projects': {
            'Meta': {'object_name': 'Projects'},
            'begin': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'beschreibung': ('django.db.models.fields.TextField', [], {}),
            'ende': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kunde': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['db.Kunde']", 'on_delete': 'models.PROTECT'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nr': ('django.db.models.fields.IntegerField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        }
    }

    complete_apps = ['db']