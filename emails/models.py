from django.db import models

# Create your models here.

from django.db import models

class EmailResponse(models.Model):
    lead = models.ForeignKey('leads.Lead', on_delete=models.CASCADE)
    opened = models.BooleanField(default=False)
    clicked = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
