from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Letter(models.Model):
    # letter id 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=False) # 제목
    body = models.TextField() # 게시물 설명
    is_public = models.BooleanField(default=False) # 익명 여부
    created_at = models.DateTimeField(auto_now_add=True) # 처음 업로드 시간

    def __str__(self):
        return self.title