from django.db import models
from accounts.models import *

class Reference(models.Model):
	from_group = models.OneToOneField(Group, on_delete=models.CASCADE, related_name="from_group")
	to_group = models.OneToOneField(Group, on_delete=models.CASCADE, related_name="to_group")
	extras = models.TextField()
	date_created = models.DateTimeField()

	def __str__(self):
		return 'From {}, to {}'.format(self.from_group, self.to_group)

class ConcreteBusiness(models.Model):
	reference = models.OneToOneField(Reference, on_delete=models.CASCADE, related_name="concrete_business")
	amount = models.DecimalField(decimal_places=2, max_digits=10)
	date = models.DateTimeField()
	extras = models.TextField()

	def __str__(self):
		return 'Reference {}'.format(self.reference)