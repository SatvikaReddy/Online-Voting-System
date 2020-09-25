from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import models
from .models import Person
from django.views.generic import CreateView
from .forms import MyModelForm
from django.urls import reverse_lazy

class PersonCreateView(CreateView):
    model = Person
    form_class = MyModelForm
    # fields = '__all__'
    success_url=reverse_lazy('accounts:success')

def success(request):
    return render(request,'accounts/success.html',{})

def home(request):
    return render(request, template_name='base.html')

@login_required
def profile(request):
    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     # user = authenticate(username=username, password=password)
    #     if user:
    #         if user.is_active and user.is_voter:
    #             return render(request, 'accounts/voter.html')
    #         if user.is_active and user.is_voter == False:
    #             return render(request, 'accounts/candidate.html')
    #     else:
    if request.user.is_voter:
        return render(request, 'accounts/voter.html')
    else:
        return render(request, 'accounts/candidate.html')