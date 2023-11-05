from django.db import models

# Create your models here.
class AccordionItem(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title