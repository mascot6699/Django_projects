from django.db import models

# Create your models here.

class LogEntry(models.Model):
	"""
	Defination of a LogEntry
	"""
	timestamp = models.DateTimeField(auto_now_add=True)
	severity  = models.CharField(blank=False,max_lenght=10)
	message   = models.TextField(blank=False)
	