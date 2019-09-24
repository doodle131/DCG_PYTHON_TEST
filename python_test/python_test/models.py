# required packages 
from django.db import models
from django_extensions.db.models import TimeStampedModel

# model Client

class Client(TimeStampedModel, models.Model): 
	"""
	    We could have also created a created update model
	    by extending models.Model to track created by and 
	    update by User  
	"""
	name = models.CharField(max_length=250, blank=False, null=False, db_index=True, unique=True)
	# could have been textfields instead of charfield but totally depends upon the usecase or historic data   
	street_name = models.CharField(max_length=255)
	suburb = models.CharField(max_length=255)
	postcode = models.CharField(max_length=15)
	# could have used a Positive Integer field to show a dropdown of available states insted of taking a plain text entry
	state = models.CharField(max_length=255)
	contact_name = models.CharField(max_length=255)
	email_address = models.CharField(max_length=255, blank=False, null=False)
	phone_number = models.CharField(max_length=20, blank=False, null=False)
	
	def __str__(self):
		return "{}".format(self.name)



