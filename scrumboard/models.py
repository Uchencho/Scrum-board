from django.db import models

# Create your models here.
class List(models.Model):
    name = models.CharField(max_length=50)

    #Used for fine naming
    def __str__(self):
        return "list: {}".format(self.name)


class Card(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    the_list = models.ForeignKey(List, on_delete=models.PROTECT, related_name='cards')
    story_points = models.IntegerField(null=True, blank=True)
    business_value = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return "Card {}".format(self.title)