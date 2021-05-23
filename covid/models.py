from django.db import models

# Create your models here.
class TestDetail(models.Model):
    user_name = models.CharField(max_length=50,null=True,verbose_name="name:")
    result = models.CharField(max_length=50,null=True,verbose_name="result:")
    cough = models.IntegerField(null=True,verbose_name="cough:")
    fever = models.IntegerField(null=True,verbose_name="fever:")
    sore = models.IntegerField(null=True,verbose_name="sore:")
    male = models.IntegerField(null=True,verbose_name="male:")
    breath = models.IntegerField(null=True,verbose_name="breath:")
    head = models.IntegerField(null=True,verbose_name="head:")
    older = models.IntegerField(null=True,verbose_name="older:")
    patient = models.IntegerField(null=True,verbose_name="patient:")

    def __str__(self):
        return self.user_name
