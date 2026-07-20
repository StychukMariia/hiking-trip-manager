from django import forms
from django.contrib.auth import get_user_model

from hikes.models import Expedition


class ExpeditionForm(forms.ModelForm):
    hikers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Expedition
        fields = "__all__"
