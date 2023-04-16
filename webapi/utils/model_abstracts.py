import uuid
from django.db import models


class Model(models.Model):
    """
    modified models to use uuid4 instead of id field
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    class Meta:
        abstract = True