
from django.db import models

# Create your models here.
from abc import ABC, abstractmethod

class BaseEntity(ABC):
    @abstractmethod
    def validate(self):
        pass

    def to_dict(self):
        return {
            key: value
            for key, value in self.__dict__.items()
        }

class Reporter(BaseEntity):
    def __init__(self, id, name, email, team):
        self.id = id
        self.name = name
        self.email = email
        self.team = team

    def validate(self):
        if not self.name:
            raise ValueError('Name cannot be empty')
        if '@' not in self.email:
            raise ValueError('Invalid email')

# In views.py:
# from issues.models import Reporter, Issue
class Issue(BaseEntity):
    def __init__(self, id, title, description, status,  priority, reporter_id, created_at=None):
        self.id = id
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority
        self.reporter_id = reporter_id
        self.created_at = created_at

    def validate(self):
        if not self.title:
            raise ValueError('Title is required')
        if not self.status:
            raise ValueError('Status is required')
        if not self.priority:
            raise ValueError('Priority is required')


class CriticalIssue(Issue):

    def describe(self):
        return f"[URGENT] {self.title} - needs immediate attention"

class LowPriorityIssue(Issue):

    def describe(self):
        return f"{self.title} - low priority, handle when free"

