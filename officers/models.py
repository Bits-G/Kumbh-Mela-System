from django.db import models


# ===== PR / GO / PSE / Other Hierarchy =====

MAIN_TYPE_CHOICES = [
    ('pr', 'Public Representative (PR)'),
    ('go', 'Government Officials (GO)'),
    ('pse', 'Private Sector Executives (PSE)'),
    ('other', 'Other'),
]

SUB_TYPE_MAP = {
    'pr': [
        ('pr_central_govt', 'Central Government'),
        ('pr_state_govt', 'State Government'),
        ('pr_local_urban', 'Local Bodies (Urban)'),
        ('pr_local_rural', 'Local Bodies (Rural)'),
        ('pr_psu', 'Public Sector Unit (PSU)'),
        ('pr_other', 'Other'),
    ],
    'go': [
        ('go_central_govt', 'Central Government'),
        ('go_state_govt', 'State Government'),
        ('go_local_urban', 'Local Bodies (Urban)'),
        ('go_local_rural', 'Local Bodies (Rural)'),
        ('go_psu', 'Public Sector Unit (PSU)'),
        ('go_other', 'Other'),
    ],
    'pse': [
        ('pse_corporate', 'Corporate'),
        ('pse_organisation', 'Organisation'),
        ('pse_individual', 'Individual'),
    ],
    'other': [],
}

SUB_SUB_TYPE_MAP = {
    'pr_central_govt': [
        ('president', 'President'),
        ('prime_minister', 'Prime Minister'),
        ('cabinet_minister', 'Cabinet Minister'),
        ('state_minister', 'State Minister'),
        ('mp_loksabha', 'MP Loksabha'),
        ('mp_rajyasabha', 'MP Rajyasabha'),
        ('central_board_committee', 'Central Board/Committee'),
    ],
    'pr_state_govt': [
        ('governor', 'Governor'),
        ('chief_minister', 'Chief Minister'),
        ('deputy_chief_minister', 'Deputy Chief Minister'),
        ('cabinet_minister', 'Cabinet Minister'),
        ('state_minister', 'State Minister'),
        ('mla', 'MLA'),
        ('mlc', 'MLC'),
        ('state_board_committee', 'State Board/Committee'),
    ],
    'pr_local_urban': [
        ('mayor', 'Mayor'),
        ('deputy_mayor', 'Deputy Mayor'),
        ('president', 'President'),
        ('vice_president', 'Vice President'),
        ('corporator', 'Corporator'),
        ('councillor', 'Councillor'),
    ],
    'pr_local_rural': [
        ('zp_president', 'ZP President'),
        ('zp_vice_president', 'ZP Vice President'),
        ('zp_member', 'ZP Member'),
        ('ps_president', 'PS President'),
        ('ps_vice_president', 'PS Vice President'),
        ('ps_member', 'PS Member'),
        ('gp', 'GP'),
    ],
    'pr_psu': [
        ('chairman', 'Chairman'),
        ('vice_chairman', 'Vice Chairman'),
        ('president', 'President'),
        ('vice_president', 'Vice President'),
        ('director', 'Director'),
        ('member', 'Member'),
    ],
    'pr_other': [
        ('other', 'Other'),
    ],
    'go_central_govt': [],
    'go_state_govt': [
        ('mantralay', 'Mantralay'),
        ('divisional_commissioner_office', 'Divisional Commissioner Office'),
        ('collector_office', 'Collector Office'),
        ('sub_divisional_office', 'Sub Divisional Office'),
        ('tahsil_office', 'Tahsil Office'),
        ('department', 'Department'),
    ],
    'go_local_urban': [
        ('municipal_corporation_office', 'Municipal Corporation Office'),
        ('municipal_council_office', 'Municipal Council Office'),
    ],
    'go_local_rural': [
        ('zp_office', 'ZP Office'),
        ('ps_office', 'PS Office'),
        ('gp_office', 'GP Office'),
    ],
    'go_psu': [],
    'go_other': [],
    'pse_corporate': [],
    'pse_organisation': [],
    'pse_individual': [],
}

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

    main_type = models.CharField("Main Type", max_length=20, blank=True, null=True)
    sub_type = models.CharField("Sub Type", max_length=50, blank=True, null=True)
    sub_sub_type = models.CharField("Sub-Sub Type", max_length=50, blank=True, null=True)
    division = models.CharField("Division (विभाग)", max_length=50, choices=DIVISION_CHOICES, blank=True, null=True)
    government_level = models.CharField("Govt Level", max_length=20, choices=GOVT_LEVEL_CHOICES, blank=True, null=True)
    department = models.CharField("Department (शाखा)", max_length=255, blank=True, null=True)
    category = models.CharField("Category (जात)", max_length=100, blank=True, null=True)
    sub_category = models.CharField("Sub-Category (पोटजात)", max_length=100, blank=True, null=True)
    contact_2 = models.CharField("Contact 2", max_length=15, blank=True, null=True)
    email = models.EmailField("Email", max_length=255, blank=True, null=True)
    office_phone = models.CharField("Office Phone", max_length=20, blank=True, null=True)
    pbx_extension = models.CharField("PBX Extension", max_length=20, blank=True, null=True)
    photo = models.ImageField("Photo", upload_to='officer_photos/', blank=True, null=True)

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