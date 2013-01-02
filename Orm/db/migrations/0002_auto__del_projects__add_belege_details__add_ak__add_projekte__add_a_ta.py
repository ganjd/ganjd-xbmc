# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Projects'
        db.delete_table('db_projects')

        # Adding model 'Belege_Details'
        db.create_table('db_belege_details', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nr', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['db.Belege'])),
            ('bezeichnung', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('menge', self.gf('django.db.models.fields.IntegerField')()),
            ('einheit', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('brutto', self.gf('django.db.models.fields.FloatField')()),
            ('netto', self.gf('django.db.models.fields.FloatField')()),
            ('projekt', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['db.Projekte'])),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal('db', ['Belege_Details'])

        # Adding model 'AK'
        db.create_table('db_ak', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('a_tag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['db.A_Tag'])),
            ('ak', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('beginn', self.gf('django.db.models.fields.TimeField')()),
            ('ende', self.gf('django.db.models.fields.TimeField')()),
            ('pause', self.gf('django.db.models.fields.IntegerField')()),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal('db', ['AK'])

        # Adding model 'Projekte'
        db.create_table('db_projekte', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nr', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('kunde', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['db.Kunde'], on_delete=models.PROTECT)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('beschreibung', self.gf('django.db.models.fields.TextField')()),
            ('begin', self.gf('django.db.models.fields.DateField')(null=True)),
            ('ende', self.gf('django.db.models.fields.DateField')(null=True)),
        ))
        db.send_create_signal('db', ['Projekte'])

        # Adding model 'A_Tag'
        db.create_table('db_a_tag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('projekt', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['db.Projekte'], on_delete=models.PROTECT)),
            ('datum', self.gf('django.db.models.fields.DateField')()),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('anzahl_ak', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('db', ['A_Tag'])

        # Adding model 'Belege'
        db.create_table('db_belege', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nr', self.gf('django.db.models.fields.IntegerField')()),
            ('datum', self.gf('django.db.models.fields.DateField')()),
            ('lieferant', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('zahlungsart', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('brutto', self.gf('django.db.models.fields.FloatField')()),
            ('netto', self.gf('django.db.models.fields.FloatField')()),
            ('anzahl_artikel', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('db', ['Belege'])


    def backwards(self, orm):
        # Adding model 'Projects'
        db.create_table('db_projects', (
            ('status', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('begin', self.gf('django.db.models.fields.DateField')(null=True)),
            ('ende', self.gf('django.db.models.fields.DateField')(null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('kunde', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['db.Kunde'], on_delete=models.PROTECT)),
            ('nr', self.gf('django.db.models.fields.IntegerField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('beschreibung', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('db', ['Projects'])

        # Deleting model 'Belege_Details'
        db.delete_table('db_belege_details')

        # Deleting model 'AK'
        db.delete_table('db_ak')

        # Deleting model 'Projekte'
        db.delete_table('db_projekte')

        # Deleting model 'A_Tag'
        db.delete_table('db_a_tag')

        # Deleting model 'Belege'
        db.delete_table('db_belege')


    models = {
        'db.a_tag': {
            'Meta': {'object_name': 'A_Tag'},
            'anzahl_ak': ('django.db.models.fields.IntegerField', [], {}),
            'datum': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'projekt': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['db.Projekte']", 'on_delete': 'models.PROTECT'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        'db.ak': {
            'Meta': {'object_name': 'AK'},
            'a_tag': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['db.A_Tag']"}),
            'ak': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'beginn': ('django.db.models.fields.TimeField', [], {}),
            'ende': ('django.db.models.fields.TimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pause': ('django.db.models.fields.IntegerField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        'db.belege': {
            'Meta': {'object_name': 'Belege'},
            'anzahl_artikel': ('django.db.models.fields.IntegerField', [], {}),
            'brutto': ('django.db.models.fields.FloatField', [], {}),
            'datum': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lieferant': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'netto': ('django.db.models.fields.FloatField', [], {}),
            'nr': ('django.db.models.fields.IntegerField', [], {}),
            'zahlungsart': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'db.belege_details': {
            'Meta': {'object_name': 'Belege_Details'},
            'bezeichnung': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'brutto': ('django.db.models.fields.FloatField', [], {}),
            'einheit': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menge': ('django.db.models.fields.IntegerField', [], {}),
            'netto': ('django.db.models.fields.FloatField', [], {}),
            'nr': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['db.Belege']"}),
            'projekt': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['db.Projekte']"}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
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
        'db.projekte': {
            'Meta': {'object_name': 'Projekte'},
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