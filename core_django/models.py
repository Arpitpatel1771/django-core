from django.contrib.admin.models import ADDITION, CHANGE, LogEntry
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from django_enumfield import enum

from core_django.enums import Status


class LogEntryCustom(LogEntry):
    object_data = models.JSONField(
        verbose_name="object_data", encoder=DjangoJSONEncoder
    )

    class Meta:
        app_label = "core_django"
        db_table = "core_django_logentrycustom"


class BaseModel(models.Model):
    status = enum.EnumField(enum=Status, default=Status.ACTIVE)
    creation_date = models.DateTimeField(auto_now_add=True)
    creation_by = models.BigIntegerField(null=True)
    updation_date = models.DateTimeField(auto_now=True)
    updation_by = models.BigIntegerField(null=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs) -> None:
        # TODO: make it so that all data which is changed gets stoored in LogEntryCustom

        return super().save(*args, **kwargs)
