# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Author'
        db.create_table(u'bookshelf_author', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'bookshelf', ['Author'])

        # Adding model 'Collection'
        db.create_table(u'bookshelf_collection', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'bookshelf', ['Collection'])

        # Adding model 'Editor'
        db.create_table(u'bookshelf_editor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'bookshelf', ['Editor'])

        # Adding model 'ReaderLevel'
        db.create_table(u'bookshelf_readerlevel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'bookshelf', ['ReaderLevel'])

        # Adding model 'Book'
        db.create_table(u'bookshelf_book', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('subtitle', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bookshelf.Author'])),
            ('illustrator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='book_illustrator_set', null=True, to=orm['bookshelf.Author'])),
            ('collection', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bookshelf.Collection'], null=True)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('reader_level', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bookshelf.ReaderLevel'])),
            ('nb_pages', self.gf('django.db.models.fields.IntegerField')()),
            ('synopsis', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'bookshelf', ['Book'])


    def backwards(self, orm):
        # Deleting model 'Author'
        db.delete_table(u'bookshelf_author')

        # Deleting model 'Collection'
        db.delete_table(u'bookshelf_collection')

        # Deleting model 'Editor'
        db.delete_table(u'bookshelf_editor')

        # Deleting model 'ReaderLevel'
        db.delete_table(u'bookshelf_readerlevel')

        # Deleting model 'Book'
        db.delete_table(u'bookshelf_book')


    models = {
        u'bookshelf.author': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Author'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'bookshelf.book': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Book'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bookshelf.Author']"}),
            'collection': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bookshelf.Collection']", 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'illustrator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'book_illustrator_set'", 'null': 'True', 'to': u"orm['bookshelf.Author']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'nb_pages': ('django.db.models.fields.IntegerField', [], {}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'reader_level': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bookshelf.ReaderLevel']"}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'synopsis': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'bookshelf.collection': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Collection'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'bookshelf.editor': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Editor'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'bookshelf.readerlevel': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'ReaderLevel'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['bookshelf']