from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms
import account.forms
import account.views
from .models import Competition, Sportsman, Team
from django.views.generic import DetailView, ListView


def home(request):
    comp = Competition.objects.order_by("-comp_time")
    return render(request, 'homepage.html', {'comp': comp})

class CompDetailView(DetailView):
    model = Competition
    template_name = 'competition/detail_view.html'
    context_object_name = 'comp_element'


@login_required
def my_team(request):
    error = ''
    if request.method == 'POST':
        form = forms.TeamForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Введенные данные некорректны, попробуйте еще раз.'

    form = forms.TeamForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'competition/team.html', data)


@login_required
def add_sprtmn(request):
    error = ''
    if request.method == 'POST':
        form = forms.SprtmnForm(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.trainer = request.user
            temp.save()
        else:
            error = 'Введенные данные некорректны'

    form = forms.SprtmnForm()

    sprtmn = Sportsman.objects.filter(trainer=request.user).order_by("dob")

    data = {
        'form': form,
        'error': error,
        'sprtmn': sprtmn,
    }

    return render(request, 'competition/sportsmen_list.html', data)


@login_required
def parcticipants_registration(request):
    error = ''
    user_list = Sportsman.objects.filter(trainer=request.user).order_by("dob")

    data = {
        # 'form': form,
        'error': error,
        'user_list': user_list,
    }

    return render(request, 'competition/participants_registration.html', data)


@login_required
def add_comp(request):
    error = ''
    if request.method == 'POST':
        form = forms.CompForm(request.POST, request.FILES)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.owner = request.user
            temp.save()

            return redirect('/')
        else:
            error = 'Введенные данные некорректны'

    form = forms.CompForm()

    data = {
        'form': form,
        'error': error,
    }

    return render(request, 'competition/add_one.html', data)


class Search(ListView):

    model = Competition

    def get_queryset(self):
        return Competition.objects.filter(title__icontains=self.request.GET.get("q")).order_by("-comp_time")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get("q")
        return context


class MyCompList(ListView):

    model = Competition

    def get_queryset(self):
        return Competition.objects.filter(owner=self.request.user).order_by("-comp_time")


class LoginView(account.views.LoginView):
    form_class = account.forms.LoginEmailForm


class SignupView(account.views.SignupView):

    form_class = forms.SignupForm

    def after_signup(self, form):
        # do something
        super(SignupView, self).after_signup(form)