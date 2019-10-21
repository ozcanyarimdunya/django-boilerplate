from django.db import models


class BaseModel(models.Model):
    """
    BaseModel
    =========
    A Base TimeStamped model with extras field
    All models will inherit BaseModel
    """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
