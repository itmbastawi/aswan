from django.db import models
from utils.model_abstracts import Model
from django_extensions.db import models as ext_models

class Contact(
    ext_models.TimeStampedModel,
    ext_models.ActivatorModel,
    ext_models.TitleDescriptionModel,
    Model
    ):

    class Meta:
        verbose_name_plural = "contacts"

    email = models.EmailField(verbose_name = "Email")
    def __str__(self) -> str:
        return f"{self.title}"
    

    