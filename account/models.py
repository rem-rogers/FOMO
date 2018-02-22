from django.db import models
from cuser.models import AbstractCUser


# Create your models here.
class User(AbstractCUser):

   salary = models.IntegerField(null=True, blank=True)
   birthdate = models.TextField(null=True, blank=True)
   address = models.TextField(null=True, blank=True)
   city = models.TextField(null=True, blank=True)
   state = models.TextField(null=True, blank=True)
   zip = models.TextField(null=True, blank=True)

   def get_purchases(self):
      return ['Roku', 'kindle fire']