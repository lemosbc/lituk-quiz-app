from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class QuesModel(models.Model):
    question = models.CharField(max_length=200,null=True)
    question_id = models.AutoField(primary_key=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.question
    
class UserResults(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    result = models.IntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.user_id} "
            f"{self.result} "
            f"({self.created:%Y-%m-%d %H:%M}): "
        )