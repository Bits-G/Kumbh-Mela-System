# from django import forms
# from .models import Officer


# class OfficerForm(forms.ModelForm):
#     class Meta:
#         model = Officer
#         fields = ['name', 'mobile_number', 'designation', 'city', 'state', 'address', 'work']
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'पूरा नाम दर्ज करें'}),
#             'mobile_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '10 अंकों का मोबाइल नंबर'}),
#             'designation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'अधिकारी पद'}),
#             'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'शहर'}),
#             'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'राज्य'}),
#             'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'पूरा पता'}),
#             'work': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'कार्य विवरण'}),
#         }

from django import forms
from .models import Officer, DIVISION_CHOICES, GOVT_LEVEL_CHOICES

DESIGNATION_CHOICES = [
    ("", "Select Designation"),
    ("Police Inspector", "Police Inspector"),
    ("Police Constable", "Police Constable"),
    ("Medical Officer", "Medical Officer"),
    ("Health Inspector", "Health Inspector"),
    ("Fire Officer", "Fire Officer"),
    ("Traffic Inspector", "Traffic Inspector"),
    ("Volunteer Coordinator", "Volunteer Coordinator"),
    ("Registration Officer", "Registration Officer"),
    ("Data Entry Operator", "Data Entry Operator"),
    ("Control Room Operator", "Control Room Operator"),
    ("Camp Supervisor", "Camp Supervisor"),
]

STATE_CHOICES = [
    ("", "Select State"),
    ("Andhra Pradesh", "Andhra Pradesh"),
    ("Arunachal Pradesh", "Arunachal Pradesh"),
    ("Assam", "Assam"),
    ("Bihar", "Bihar"),
    ("Chhattisgarh", "Chhattisgarh"),
    ("Goa", "Goa"),
    ("Gujarat", "Gujarat"),
    ("Haryana", "Haryana"),
    ("Himachal Pradesh", "Himachal Pradesh"),
    ("Jharkhand", "Jharkhand"),
    ("Karnataka", "Karnataka"),
    ("Kerala", "Kerala"),
    ("Madhya Pradesh", "Madhya Pradesh"),
    ("Maharashtra", "Maharashtra"),
    ("Manipur", "Manipur"),
    ("Meghalaya", "Meghalaya"),
    ("Mizoram", "Mizoram"),
    ("Nagaland", "Nagaland"),
    ("Odisha", "Odisha"),
    ("Punjab", "Punjab"),
    ("Rajasthan", "Rajasthan"),
    ("Sikkim", "Sikkim"),
    ("Tamil Nadu", "Tamil Nadu"),
    ("Telangana", "Telangana"),
    ("Tripura", "Tripura"),
    ("Uttar Pradesh", "Uttar Pradesh"),
    ("Uttarakhand", "Uttarakhand"),
    ("West Bengal", "West Bengal"),
    ("Andaman and Nicobar Islands", "Andaman and Nicobar Islands"),
    ("Chandigarh", "Chandigarh"),
    ("Dadra and Nagar Haveli and Daman and Diu", "Dadra and Nagar Haveli and Daman and Diu"),
    ("Delhi", "Delhi"),
    ("Jammu and Kashmir", "Jammu and Kashmir"),
    ("Ladakh", "Ladakh"),
    ("Lakshadweep", "Lakshadweep"),
    ("Puducherry", "Puducherry"),
]

CITY_CHOICES = [
    ("", "Select City"),
    ("Agra", "Agra"),
    ("Ahmedabad", "Ahmedabad"),
    ("Ajmer", "Ajmer"),
    ("Aligarh", "Aligarh"),
    ("Amravati", "Amravati"),
    ("Amritsar", "Amritsar"),
    ("Aurangabad", "Aurangabad"),
    ("Bengaluru", "Bengaluru"),
    ("Bhopal", "Bhopal"),
    ("Bhubaneswar", "Bhubaneswar"),
    ("Chandigarh", "Chandigarh"),
    ("Chennai", "Chennai"),
    ("Coimbatore", "Coimbatore"),
    ("Cuttack", "Cuttack"),
    ("Dehradun", "Dehradun"),
    ("Delhi", "Delhi"),
    ("Dhanbad", "Dhanbad"),
    ("Durgapur", "Durgapur"),
    ("Faridabad", "Faridabad"),
    ("Ghaziabad", "Ghaziabad"),
    ("Gorakhpur", "Gorakhpur"),
    ("Guntur", "Guntur"),
    ("Guwahati", "Guwahati"),
    ("Gwalior", "Gwalior"),
    ("Haridwar", "Haridwar"),
    ("Hubli", "Hubli"),
    ("Hyderabad", "Hyderabad"),
    ("Indore", "Indore"),
    ("Jabalpur", "Jabalpur"),
    ("Jaipur", "Jaipur"),
    ("Jalandhar", "Jalandhar"),
    ("Jammu", "Jammu"),
    ("Jamnagar", "Jamnagar"),
    ("Jamshedpur", "Jamshedpur"),
    ("Jodhpur", "Jodhpur"),
    ("Kanpur", "Kanpur"),
    ("Kochi", "Kochi"),
    ("Kolhapur", "Kolhapur"),
    ("Kolkata", "Kolkata"),
    ("Kota", "Kota"),
    ("Lucknow", "Lucknow"),
    ("Ludhiana", "Ludhiana"),
    ("Madurai", "Madurai"),
    ("Meerut", "Meerut"),
    ("Mumbai", "Mumbai"),
    ("Mysuru", "Mysuru"),
    ("Nagpur", "Nagpur"),
    ("Nashik", "Nashik"),
    ("Navi Mumbai", "Navi Mumbai"),
    ("Noida", "Noida"),
    ("Patna", "Patna"),
    ("Pimpri-Chinchwad", "Pimpri-Chinchwad"),
    ("Prayagraj", "Prayagraj"),
    ("Pune", "Pune"),
    ("Raipur", "Raipur"),
    ("Rajkot", "Rajkot"),
    ("Ranchi", "Ranchi"),
    ("Rourkela", "Rourkela"),
    ("Siliguri", "Siliguri"),
    ("Solapur", "Solapur"),
    ("Srinagar", "Srinagar"),
    ("Surat", "Surat"),
    ("Thane", "Thane"),
    ("Tiruchirappalli", "Tiruchirappalli"),
    ("Udaipur", "Udaipur"),
    ("Ujjain", "Ujjain"),
    ("Vadodara", "Vadodara"),
    ("Varanasi", "Varanasi"),
    ("Vijayawada", "Vijayawada"),
    ("Visakhapatnam", "Visakhapatnam"),
    ("Warangal", "Warangal"),
]

WORK_CHOICES = [
    ("", "Select Work"),
    ("Crowd Control", "Crowd Control"),
    ("Traffic Management", "Traffic Management"),
    ("Security Duty", "Security Duty"),
    ("Emergency Medical Services", "Emergency Medical Services"),
    ("Volunteer Management", "Volunteer Management"),
    ("Registration", "Registration"),
    ("Lost & Found", "Lost & Found"),
    ("Fire Safety", "Fire Safety"),
    ("Sanitation Management", "Sanitation Management"),
    ("IT Support", "IT Support"),
]


class OfficerForm(forms.ModelForm):

    designation = forms.CharField(
    widget=forms.TextInput(attrs={
        'class': 'form-control',
        'list': 'designation-list',
        'placeholder': 'Search or enter designation'
    })
)

    state = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'list': 'state-list',
            'placeholder': 'Search or Enter state'})
    )
    
    city = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'list': 'city-list',
            'placeholder': 'Search or Enter city'})
    )

    work = forms.CharField(
        # choices=WORK_CHOICES,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'list': 'work-list',
            'placeholder': 'Search or Enter work'
        })
    )

    division = forms.ChoiceField(
        choices=[("", "Select Division")] + DIVISION_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    government_level = forms.ChoiceField(
        choices=[("", "Select Govt Level")] + GOVT_LEVEL_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Officer
        fields = ['name', 'mobile_number', 'designation', 'state', 'city', 'address', 'work', 'division', 'government_level']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'पूरा नाम दर्ज करें'
            }),

            'mobile_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '10 अंकों का मोबाइल नंबर'
            }),

            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'पूरा पता'
            }),
        }