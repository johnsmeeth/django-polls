import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
'''
	Create a model named Question extended from parent class django.db.models.Model. Question models
	has two field is question_text and pub_date, they are created with some parameter as:
		+ max_length: this is specify length of field, this is used in validation.
		+ 'date published': Used to define a human-readable name for a field. And other field not specify
			human- readable name, django will auto assign a machine-readable name. and a tiny note:
			It always take the first position in parameters list
	Every fields is belong about one type of field was defined in django.db.models. As we see we 
	have some field type as: CharField, DateTimeField, IntegerField and a special field is ForeignKey
	was used in question field on Choice mode: this tell django each Choice is related to a single 
	Question. And django support popular relate type: many-to-many, many-to-one, one-to-one.
'''
class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published', default=timezone.now)

	# __unicode__(__str__ on python 3): return unicode value
	def __unicode__(self): 
		return self.question_text

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

	# Improve display possible of was_published_recently on admin
	### admin_order_field not work if change to 'question_text' or commented: 
	### i am not yet understand, perhap cause is
	### in admin.py we indicated order to display in option list_display
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __unicode__(self):
		return self.choice_text


