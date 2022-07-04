from django import forms
from django.utils.translation import ugettext_lazy as _

from randevu.models import Randevu
from hasta.models import Hasta


class RandevuCreateForm(forms.ModelForm):
    class Meta:
        model = Randevu
        exclude = ["state"]
        widgets = {
            "hasta": forms.widgets.TextInput(attrs={"class": "form-control"}),
            "date": forms.widgets.DateInput(attrs={"class": "form-control datepicker"}),
            "time": forms.widgets.TimeInput(attrs={"class": "form-control"}),
            "person_number": forms.widgets.NumberInput(attrs={"class": "form-control"}),
            "contact_phone": forms.widgets.TextInput(attrs={"class": "form-control"}),
        }
        labels = {
            "hasta": _("Hasta"),
            "date": _("Tarih"),
            "time": _("Saat"),
            "person_number": _("Kişi sayısı"),
            "contact_phone": _("İrtibat No"),
        }

    def __init__(self, *args, **kwargs):
        super(RandevuCreateForm, self).__init__(*args, **kwargs)
        self.fields["contact_phone"].required = False
        self.fields["person_number"].required = False
