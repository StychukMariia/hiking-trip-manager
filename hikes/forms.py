from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from hikes.models import Expedition, Hiker


class ExpeditionForm(forms.ModelForm):
    hikers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Expedition
        fields = "__all__"


class HikerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Hiker
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "fitness_level",
            "has_tent",
        )


class HikerUpdateForm(forms.ModelForm):
    class Meta:
        model = Hiker
        fields = ["fitness_level", "has_tent"]


class HikerUsernameSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by username"}
        ),
    )


class RegionNameSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by name"}
        )
    )


class ExpeditionTitleSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by title"}
        )
    )
