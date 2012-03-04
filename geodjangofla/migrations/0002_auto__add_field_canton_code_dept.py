# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Canton.code_dept'
        db.add_column('geodjangofla_canton', 'code_dept', self.gf('django.db.models.fields.CharField')(default=0, max_length=2), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Canton.code_dept'
        db.delete_column('geodjangofla_canton', 'code_dept')


    models = {
        'geodjangofla.arrondissement': {
            'Meta': {'ordering': "('departement', 'code_arr')", 'object_name': 'Arrondissement'},
            'centroid': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'chf_lieu': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'code_arr': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'code_chf': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'departement': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['geodjangofla.Departement']", 'null': 'True', 'blank': 'True'}),
            'id_geofla': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'limite': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'null': 'True', 'blank': 'True'}),
            'nom_chf': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'geodjangofla.canton': {
            'Meta': {'ordering': "('arrondissement', 'code_cant')", 'object_name': 'Canton'},
            'arrondissement': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['geodjangofla.Arrondissement']", 'null': 'True', 'blank': 'True'}),
            'centroid': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'chf_lieu': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'code_cant': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'code_chf': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'code_dept': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'id_geofla': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'limite': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'null': 'True', 'blank': 'True'}),
            'nom_chf': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'geodjangofla.commune': {
            'Meta': {'object_name': 'Commune'},
            'canton': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['geodjangofla.Canton']", 'null': 'True', 'blank': 'True'}),
            'centroid': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'chf_lieu': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'code_comm': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'id_geofla': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'insee_com': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'limite': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'null': 'True', 'blank': 'True'}),
            'nom_comm': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'population': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'statut': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'superficie': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'z_moyen': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'geodjangofla.departement': {
            'Meta': {'ordering': "('nom_dept',)", 'object_name': 'Departement'},
            'centroid': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'chf_lieu': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'code_chf': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'code_dept': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'id_geofla': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'limite': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'null': 'True', 'blank': 'True'}),
            'nom_chf': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'nom_dept': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['geodjangofla.Region']", 'null': 'True', 'blank': 'True'})
        },
        'geodjangofla.region': {
            'Meta': {'ordering': "('nom_region',)", 'object_name': 'Region'},
            'code_reg': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'id_geofla': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nom_region': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['geodjangofla']
