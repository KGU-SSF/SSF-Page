from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class join(models.Model):
    applications_name = models.CharField(max_length=10)
    apllications_studentID = models.IntegerField(default=0)
    applications_phoneNumberRegex = RegexValidator(regex = r'^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$')
    applications_phoneNumber = models.CharField(validators=[applications_phoneNumberRegex], max_length=11, unique=True)
    applications_text = models.TextField()

    #객체 이름 = 사용자 이름
    def __str__(self):
        return self.applications_name
