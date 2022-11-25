from django.db import models
from mptt.models import MPTTModel,TreeForeignKey
# Create your models here.

class Genre(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']
