from django.db import models

# Create your models here.
ch = (('yes','yes'),
      ('no','no')
      )
class Contact(models.Model):
    Name = models.CharField(max_length=50)
    Phone = models.CharField(max_length=15)
    Email = models.EmailField(max_length=256)
    Address = models.TextField()
    Date = models.DateTimeField(auto_now=False,auto_now_add=False)
    Reason = models.TextField()
    Call_back = models.CharField(max_length=5,choices=ch)

    def __str__(self):
        return self.Name