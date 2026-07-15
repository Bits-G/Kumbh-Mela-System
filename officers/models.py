from django.db import models


DIVISION_CHOICES = [
    ('education', 'Education (शिक्षा)'),
    ('health', 'Health (आरोग्य)'),
    ('transport', 'Transport (वाहतूक)'),
    ('security', 'Security (सुरक्षा)'),
    ('sanitation', 'Sanitation (स्वच्छता)'),
    ('district_office', 'District Office (जिल्हाधिकारी कार्यालय)'),
    ('divisional_commissioner', 'Divisional Commissioner Office (विभागीय आयुक्त कार्यालय)'),
    ('kumbh_authority', 'Kumbh Mela Authority'),
    ('police', 'Police (पोलीस)'),
    ('other', 'Other'),
]

GOVT_LEVEL_CHOICES = [
    ('central', 'Central Govt'),
    ('state', 'State Govt'),
]


class Officer(models.Model):
    name = models.CharField("Name (नाम)", max_length=255)
    mobile_number = models.CharField("Mobile Number (नंबर)", max_length=15)
    designation = models.CharField("अधिकारी पद", max_length=255)
    state = models.CharField("State (राज्य)", max_length=100)
    city = models.CharField("City (शहर)", max_length=100)
    address = models.TextField("Address (पत्ता)")
    work = models.TextField("Work (काम)")

    division = models.CharField("Division (विभाग)", max_length=50, choices=DIVISION_CHOICES, blank=True, null=True)
    government_level = models.CharField("Govt Level", max_length=20, choices=GOVT_LEVEL_CHOICES, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['mobile_number']),
            models.Index(fields=['state']),
            models.Index(fields=['city']),
            models.Index(fields=['designation']),
            models.Index(fields=['division']),
        ]
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.designation})"