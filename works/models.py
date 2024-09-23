from django.db import models

# Create your models here.
from django.db import models

class Work(models.Model):
    CATEGORY_CHOICES = (
        ("1","365Alert"),
        ("2,","WISE Audit")
    )
    work_name = models.CharField(max_length=200)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.work_name