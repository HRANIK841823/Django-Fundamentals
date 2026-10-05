from django import forms
from django.forms.widgets import NumberInput
from django.forms.widgets import TextInput
BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
import datetime
class ExampleForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    comment = forms.CharField(widget=forms.Textarea)
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    agree = forms.BooleanField(initial=True)
    date = forms.DateField()
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    value = forms.DecimalField()
    message = forms.CharField(
	max_length = 10,
    )
    email_address = forms.EmailField( 
    label="Please enter your email address",
    )
    first_name=forms.CharField(initial='Your Name')
    day = forms.DateField(initial=datetime.date.today)
    
    FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
    ]
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_color_radio_select = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    favorite_colors_multiple_choicefield = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_colors_checkbox = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES,)
    roll_number = forms.IntegerField( 
                     help_text = "Enter 6 digit roll number"
                     )
    password = forms.CharField(widget = forms.PasswordInput()) 
    
    datetime= forms.DateTimeField(
        input_formats=['%Y-%m-%d %H:%M:%S'],
        widget=TextInput(attrs={'style': 'width: 200px;', 'placeholder': 'YYYY-MM-DD HH:MM:SS'})
    )
    submit_duration=forms.DurationField()
    file_submit=forms.FileField()
    image=forms.ImageField()
    Ip=forms.GenericIPAddressField()
    Time=forms.TimeField()
    URL_Field=forms.URLField()




    