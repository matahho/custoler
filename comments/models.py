from django.db import models

# Create your models here.


class Comment(models.Model):
    id = models.BigIntegerField(primary_key=True)
    created = models.DateTimeField()
    username = models.CharField(max_length=255)
    text = models.TextField()
    likes = models.IntegerField(default=0)
    answers = models.JSONField()
    post_id = models.CharField(max_length=255, default=None)

    def __str__(self):
        return str(self.text[0:100])
