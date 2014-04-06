# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table(u'summit_app_userprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('points', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('occupation', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('identity', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal(u'summit_app', ['UserProfile'])

        # Adding model 'Content'
        db.create_table(u'summit_app_content', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('content_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('is_toplevel_question', self.gf('django.db.models.fields.BooleanField')()),
            ('top_level_question', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='children_of_top_level', null=True, to=orm['summit_app.Content'])),
            ('parent_content', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='comment_parent_child', null=True, to=orm['summit_app.Content'])),
            ('children', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='parent', null=True, to=orm['summit_app.Content'])),
            ('endorse_rating', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('content_rating', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('insight_rating', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('star_rating', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'summit_app', ['Content'])

        # Adding model 'BoK'
        db.create_table(u'summit_app_bok', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('headline', self.gf('django.db.models.fields.TextField')()),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('arguments', self.gf('django.db.models.fields.TextField')()),
            ('support', self.gf('django.db.models.fields.TextField')()),
            ('citations', self.gf('django.db.models.fields.TextField')()),
            ('bok_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('parent_content', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['summit_app.Content'])),
            ('endorse_rating', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('content_rating', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('insight_rating', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'summit_app', ['BoK'])


    def backwards(self, orm):
        # Deleting model 'UserProfile'
        db.delete_table(u'summit_app_userprofile')

        # Deleting model 'Content'
        db.delete_table(u'summit_app_content')

        # Deleting model 'BoK'
        db.delete_table(u'summit_app_bok')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'codename',)", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'summit_app.bok': {
            'Meta': {'object_name': 'BoK'},
            'arguments': ('django.db.models.fields.TextField', [], {}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'bok_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'citations': ('django.db.models.fields.TextField', [], {}),
            'content_rating': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'endorse_rating': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'headline': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insight_rating': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent_content': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['summit_app.Content']"}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'support': ('django.db.models.fields.TextField', [], {})
        },
        u'summit_app.content': {
            'Meta': {'object_name': 'Content'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'children': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'parent'", 'null': 'True', 'to': u"orm['summit_app.Content']"}),
            'content_rating': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'content_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'endorse_rating': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insight_rating': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'is_toplevel_question': ('django.db.models.fields.BooleanField', [], {}),
            'parent_content': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'comment_parent_child'", 'null': 'True', 'to': u"orm['summit_app.Content']"}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'star_rating': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'top_level_question': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children_of_top_level'", 'null': 'True', 'to': u"orm['summit_app.Content']"})
        },
        u'summit_app.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identity': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'occupation': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'points': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['summit_app']