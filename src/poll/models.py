from django.db import models

# Create your models here.
"""
class Question (models.Model):
	question_text = models.CharFeild(max_length=200)
	pub_date = models.DateTimeFeild('date published')

class Choice (models.Model):
	question = models.ForeignKey(Question, on_delet=models.CASCADE)
	choice_text = models.CharFeild(max_length=200)
	votes = models.IntegerFeild(default=0)

"""