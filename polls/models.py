from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
import ast

class ListField(models.TextField):
    __metaclass__ = models.DurationField
    description = "Stores a python list"

    def __init__(self, *args, **kwargs):
        super(ListField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value:
            value = []

        if isinstance(value, list):
            return value

        return ast.literal_eval(value)

    def get_prep_value(self, value):
        if value is None:
            return value

        return str(value)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)

class Poll(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    question=models.TextField(default='ques')
    choice1=models.TextField()
    choice2=models.TextField()
    choice1_votes=models.IntegerField(default=0)
    percentage1=models.IntegerField(default=0)
    choice2_votes=models.IntegerField(default=0)
    percentage2=models.IntegerField(default=0)
    has_voted=models.BooleanField(default=False)
    timest=models.DateTimeField(default=now)
    voters=models.TextField(blank=True)
    def __str__(self):
        return self.question


class Vote(models.Model):
    sno=models.AutoField(primary_key=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    question=models.TextField()
    choice=models.TextField()

    def __str__(self):
        return self.user.username +'-'+ self.question + '-'+self.choice
# Create your models here.
