from django.db import models

# Create your models here.
class Poll(models.Model):
    subject = models.CharField('投票主題',max_length=200)
    created = models.DateField(auto_now_add=True)

def __str__(self):
        return  str(self.id) + ":" + self.subject


class Option(models.Model):
    poll_id = models.IntegerField()
    title = models.CharField(max_length=200)
    count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.poll_id) + ": " + self.title