from django.db import models
from django.utils import timezone

class Question(models.Model):
    text = models.CharField(max_length=255)

    publication_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def was_published_recently(self):
        now = timezone.now()
        return now - timezone.timedelta(days=1) <= self.publication_date <= now

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.text
