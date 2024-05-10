from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=250, null=False)
    des = models.CharField(max_length=1024,null=False)
    image_url = models.URLField(null=True)
    link = models.URLField(null=False)
    skills = models.ManyToManyField('Skill', related_name='projects')

    update_date = models.DateTimeField(auto_now=True)


class Skill(models.Model):
    name = models.CharField(max_length=250, null=False)
    exp = models.DecimalField(null=False, max_digits=2, decimal_places=1)

    topic = models.ForeignKey('SkillTopic',related_name='skills' ,on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name

class SkillTopic(models.Model):
    name = models.CharField(max_length=250, null=False)
