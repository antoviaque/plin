# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Book.pub_date'
        db.delete_column(u'bookshelf_book', 'pub_date')

        # Adding field 'Book.pub_year'
        db.add_column(u'bookshelf_book', 'pub_year',
                      self.gf('django.db.models.fields.IntegerField')(default=2014),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Book.pub_date'
        raise RuntimeError("Cannot reverse this migration. 'Book.pub_date' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Book.pub_date'
        db.add_column(u'bookshelf_book', 'pub_date',
                      self.gf('django.db.models.fields.DateTimeField')(),
                      keep_default=False)

        # Deleting field 'Book.pub_year'
        db.delete_column(u'bookshelf_book', 'pub_year')


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
            'collection': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bookshelf.Collection']", 'null': 'True', 'blank': 'True'}),
            'cover': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'editor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bookshelf.Editor']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'illustrator': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'book_illustrator_set'", 'null': 'True', 'to': u"orm['bookshelf.Author']"}),
            'isbn': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '13'}),
            'keywords': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['bookshelf.Keyword']", 'symmetrical': 'False'}),
            'language': ('django_languages.fields.LanguageField', [], {'max_length': '3'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'nb_pages': ('django.db.models.fields.IntegerField', [], {}),
            'pub_year': ('django.db.models.fields.IntegerField', [], {}),
            'rating_score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'rating_votes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
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
        u'bookshelf.keyword': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Keyword'},
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