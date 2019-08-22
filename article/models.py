from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    #create_time = models.DateTimeField(default=timezone.now)
    last_update_time = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1)
    is_delete = models.BooleanField(default=False)
    read_num = models.IntegerField(default=0)

    def __str__(self):
        return "<Article: %s>" % self.title