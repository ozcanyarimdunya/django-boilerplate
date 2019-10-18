from django.contrib.postgres.fields import JSONField
from django.db import models


class BaseModel(models.Model):
    """
    BaseModel
    =========
    A Base TimeStamped model with extras field
    All models will inherit BaseModel
    """
    extras = JSONField(default=dict, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
