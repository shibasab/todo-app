from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# todoリストに追加するもの
class Post(models.Model):
    title = models.CharField(max_length=200) #やること
    detail = models.TextField() #やることの詳細
    created_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def create(self):
        self.created_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title