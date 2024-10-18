from django.db import models

# Create your models here.
class Item(models.Model):
    """ Model for Item inventory which is going to 
    perform different operations
    """
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.name
