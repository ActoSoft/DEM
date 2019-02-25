from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Group(models.Model):
	name = models.CharField(max_length=50)
	address = models.TextField()
	phone = models.CharField(max_length=20, null=True, blank=True)
	image = models.ImageField(upload_to="image/%Y/%m/%d", default="default.png")
	is_active = models.BooleanField(default=True)
	date_created = models.DateTimeField(default=timezone.now)
	slug = models.SlugField(max_length=100, unique=True)

	def __str__(self):
		return '{}'.format(self.name)

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.PROTECT)
	group = models.ForeignKey('Group', on_delete=models.PROTECT)
	phone = models.CharField(max_length=20, blank=True, null=True)
	image = models.ImageField(upload_to="image/%Y/%m/%d", default="/default.png")

	def __str__(self):
		return '{}'.format(self.user)	