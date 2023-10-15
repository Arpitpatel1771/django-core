from django_enumfield import enum

class Status(enum.Enum):
    ACTIVE = 1
    INACTIVE = 2