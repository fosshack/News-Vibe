# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django_extensions.db import fields as extension_fields
from django_extensions.db.fields import AutoSlugField

from django.db import models

# Create your models here.

class news(models.Model):
	title = models.CharField(max_length = 300,default="Not available",primary_key = True)
	slug = extension_fields.AutoSlugField(populate_from='title', blank=True)
	description = models.TextField(default="Not available")
	url = models.URLField(default="Not available")
	urlToImage = models.URLField(default="Not available")
	publishedAt = models.CharField(default="Not available",max_length = 100,blank=True,null=True)
	
	

	positive = models.DecimalField(default = 0.0,max_digits = 10,decimal_places = 3)	
	negative = models.DecimalField(default = 0.0,max_digits = 10,decimal_places = 3)
	neutral = models.DecimalField(default = 0.0,max_digits = 10,decimal_places = 3)
	label = models.CharField(max_length = 300,default="Not available")
	anger = models.DecimalField(default = 0.0,max_digits = 10,decimal_places = 3)
	calm = models.DecimalField(default = 0.0,max_digits = 10,decimal_places = 3)
	fear = models.DecimalField(default = 0.0,max_digits = 10,decimal_places = 3)
	happy = models.DecimalField(default = 0.0,max_digits = 10,decimal_places = 3)
	like = models.DecimalField(default = 0.0,max_digits = 10,decimal_places = 3)
	shame = models.DecimalField(default = 0.0,max_digits = 10,decimal_places = 3)
	sure = models.DecimalField(default = 0.0,max_digits = 10,decimal_places = 3)
	surprise = models.DecimalField(default = 0.0,max_digits = 10,decimal_places = 3)
	#def get_article_id(self):
    #   		return self.id
	def __unicode__(self):
		return u'%s' % self.slug

	
	def get_slug(self):
       		return self.slug
	def __str__(self):
		return self.title
	#def get_update_url(self):
	#	return reverse('event_event_update', args=(self.slug,))
	#def get_absolute_url(self):
    #    	return reverse("sensor:plot", kwargs={"sid": self.id})
	# def __str__(self):
    #    	return self.title
    

class article(models.Model):
	title = models.CharField(max_length = 300,default="Not available",primary_key = True)
	text = models.TextField(default="Not available")
	def __str__(self):
		return self.title
	