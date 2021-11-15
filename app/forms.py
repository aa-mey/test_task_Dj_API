from django import forms
from .models import Worker
from datetime import datetime
from mptt.admin import MPTTAdminForm


class PersonForm(MPTTAdminForm):

    def calculation(self):
        total = (datetime.date(datetime.today()) - self.cleaned_data['date_start']).days*(self.cleaned_data['salary']/30)
        return total
    
    def save(self, commit=False):
        user = super(PersonForm, self).save(commit=commit)
        user.sum_salaries = PersonForm.calculation(self)
        user.save()
        return user