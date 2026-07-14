from django.db import models


class Officer(models.Model):
    name = models.CharField("Name (नाम)", max_length=255)
    mobile_number = models.CharField("Mobile Number (नंबर)", max_length=15)
    designation = models.CharField("अधिकारी पद", max_length=255)
    state = models.CharField("State (राज्य)", max_length=100)
    city = models.CharField("City (शहर)", max_length=100)
    address = models.TextField("Address (पत्ता)")
    work = models.TextField("Work (काम)")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['mobile_number']),
            models.Index(fields=['state']),
            models.Index(fields=['city']), 
            models.Index(fields=['designation']),
        ]
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.designation})"