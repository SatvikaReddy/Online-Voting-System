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
    liked = models.ManyToManyField(Account, default=None, blank=True, related_name='liked')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
    @property
    def num_likes(self):
        return self.liked.all().count()

    def get_absolute_url(self):
        return reverse('post_list')
    
LIKE_CHOICES=(
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)

class Like(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)

    def __str__(self):
        return str(self.post)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    content = models.TextField(max_length=250)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}-{}'.format(self.post.title, str(self.user.username))
    