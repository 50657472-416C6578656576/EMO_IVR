import account.forms
from django.forms import ModelForm
from .models import Competition, Sportsman, Team


class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ['title', 'club']


class SprtmnForm(ModelForm):
    class Meta:
        model = Sportsman
        fields = ['start_number', 'first_name', 'last_name', 'dob', 'about']


class CompForm(ModelForm):
    class Meta:
        model = Competition
        fields = ['title', 'description', 'comp_time', 'preview', 'full_text']


class SignupForm(account.forms.SignupForm):

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)