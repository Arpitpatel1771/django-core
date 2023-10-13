from collections.abc import Iterable
from django.db import models
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE
from django.core.serializers.json import DjangoJSONEncoder

class LogEntryCustom(LogEntry):

    object_data = models.JSONField(verbose_name="object_data", encoder=DjangoJSONEncoder)


class BaseModel(models.Model):

    status = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    creation_by = models.BigIntegerField(null=True)
    updation_date = models.DateTimeField(auto_now=True)
    updation_by = models.BigIntegerField(null=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs) -> None:
        
        # TODO: make it so that all data which is changed gets stoored in LogEntryCustom

        return super().save(*args, **kwargs)
    