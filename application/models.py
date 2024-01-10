from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=255, blank = True)
    message = models.TextField()

    def __str__(self):
        return self.name



class AllProjects(models.Model):
    projectCode = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000, blank=True, default='Project description here')
    github_link = models.URLField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "All Projects"
