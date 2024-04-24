from django.db import models
from django.utils import timezone


class CategoryChoice(models.IntegerChoices):
    HEALTH = 1, "Health"
    BILLS = 2, "Bills"
    WORKOUT = 3, "Workout"

class Category(models.Model):
	name = models.CharField(max_length=50,  choices=[(tag, tag.name) for tag in CategoryChoice], default=None)
	id = models.BigAutoField(primary_key=True)

	def __str__(self):
		return f"{self.name}"


class Todo(models.Model):
	title = models.CharField(max_length=100)
	details = models.TextField()
	date = models.DateTimeField(default=timezone.now)
	id = models.BigAutoField(primary_key=True)
	category=models.ForeignKey(Category, on_delete=models.DO_NOTHING,null=True,blank=True)


