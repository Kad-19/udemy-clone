from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/')
    pdf = models.FileField(upload_to='pdfs/', blank=True, null=True)
    description = models.TextField(blank=True)
    price = models.IntegerField(default=80)

    def __str__(self):
        return self.name
    
class PurchasedCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.course.name}"
