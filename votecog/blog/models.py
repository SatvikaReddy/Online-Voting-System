from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.urls import reverse
from accounts.models import Account

class Post(models.Model):
    # user = models.ForeignKey(Account, on_delete=models.CASCADE)
    author = models.ForeignKey(Account,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_list')
