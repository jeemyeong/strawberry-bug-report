from django.db import models
from model_utils.models import TimeStampedModel

# Create your models here.

class Show(TimeStampedModel):
    name = models.CharField(max_length=127, default="")

class Slot(TimeStampedModel):
    show = models.ForeignKey(Show, on_delete=models.CASCADE, related_name="slots")
    name = models.CharField(max_length=127, default="")