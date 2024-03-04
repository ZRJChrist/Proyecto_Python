from django import forms
from .models import Member, Court, Book

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['full_name', 'phone', 'birth_date', 'category']
        labels = {
            'full_name': 'Name and Lastname',
            'phone': 'Number Phone (123456789)',
            'birth_date': 'Birth Date',
            'category': 'Category',
        }
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name and Lastname', 'required': True}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Number Phone', 'pattern': '[0-9]{9}', 'minlength': '9', 'maxlength': '14', 'required': True}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control','type':'date' ,'placeholder': 'Birth Date', 'required': True}),
            'category': forms.Select(attrs={'class': 'form-select', 'required': True}),
        }

class CourtForm(forms.ModelForm):
    class Meta:
        model = Court
        fields = ['description', 'type']
        labels = {
            'description': 'Description',
            'type': 'Type',
        }
        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'type': forms.Select(attrs={'class': 'form-select'}),
        }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['member', 'court', 'date']
        labels = {
            'member': 'Member',
            'court': 'Court',
            'date': 'Date and time'
        }
        widgets = {
            'member': forms.Select(attrs={'class': 'form-select'}),
            'court': forms.Select(attrs={'class': 'form-select'}),
            'date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }