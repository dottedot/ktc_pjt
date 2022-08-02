from django.db import models

# Create your models here.

class Member(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=5)
    grade = models.IntegerField()


class Files(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    url = models.CharField(max_length=500)
    senior_id = models.IntegerField()
    require_date = models.DateTimeField(auto_now_add=True)


class Admission(models.Model):
    file = models.ForeignKey(Files, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    admission_date = models.DateTimeField(auto_now_add=True)
