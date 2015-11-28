from django.contrib import admin
from .models import Question, Choice 

# 2nd way:
class ChoiceInline(admin.TabularInline): # available: StackedInline, TabularInline
	model = Choice 
	extra = 3

# Custom admin form
class QuestionAdmin(admin.ModelAdmin):
	## re-ordering fields on edit form
	# fields = ['pub_date', 'question_text']

	## split form up into fieldset with ordering of fields on each fieldset
	fieldsets = [
		(None, {'fields': ['question_text']}),
		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]

	## add 2nd way above
	inlines = [ChoiceInline]

	## Default admin display list all Questions by only question_text (by call __unicode__ method -> __str__ python 3)
	## However we can custom individual fields(properties) and methods of model need to display by list_display option as below
	list_display = ('question_text', 'pub_date', 'was_published_recently')

	# create filter on  fields: Note only for field no method as in above list_display
	list_filter = ['pub_date', 'question_text']

	# Create a search field and search on list fields specificed
	search_fields = ['question_text'] # can: search_fields = ['question_text', 'pub_date']

# class ChoiceAdmin(admin.ModelAdmin):
	## Set fields display
	## if fields is a ForeignKey in this case is 'question' field. It will display __unicode__
	## __str__ on python 3 on related object (in this case will display value returned by __unicode__ method)
	## on Question object related
	# list_display = ('choice_text', 'votes', 'question')


# Register your models here.
# admin.site.register(Question)

## 1st way: to add Choices: This way is not recommend cause it inefficient (not more logic)
## So we need addable multiple choices every add each question. We'll see detail in 2nd way
# admin.site.register(Choice)

## register model with custom form
admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice, ChoiceAdmin)




"""
	Note:
		1. Relation ship between Question-Choice is: one-to-many
		2. To add Choices in admin: there are two way:
			2.1: 1st way (Traditional, normal - no recommend): admin.site.register(Choice) or admin.site.register(Choice, ChoiceAdmin)
			2.2: 2nd way (Add choices on every question when add questions - Recommended): This way is more efficient
				2.2.1: Define ChoiceInline class as above to specify some attributes
				2.2.2: Attach ChoiceInline into QuestionAdmin class as above through option inlines
				2.2.3: Register Question as normal (like as 1st) by: admin.site.register(Question, QuestionAdmin)
		3. More informations about option list_display at: https://docs.djangoproject.com/en/1.8/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display	
"""