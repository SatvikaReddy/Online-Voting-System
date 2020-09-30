from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required
from . import models
from .models import Person
from django.views.generic import CreateView
from .forms import MyModelForm
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone


# class PersonCreateView(CreateView):
#     model = Person
#     form_class = MyModelForm
#     # fields = '__all__'
#     success_url=reverse_lazy('accounts:success')

def success(request):
    return render(request,'accounts/success.html',{})


def cform(request):
    if request.method == "POST":
       form = MyModelForm(request.POST)
       if form.is_valid():
           post = form.save(commit=False)
           post.published_date = timezone.now()
           if request.user.is_authenticated:
                post.user=request.user
           post.save()
           return redirect('accounts:success')
    else:
        form = MyModelForm()
    return render(request, 'accounts/person_form.html', {'form': form})

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

def dashboard(request):
    form = Person.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'accounts/dashboard.html', {'values1': form})

@csrf_exempt
def cstatus(request,pk):
    form = get_object_or_404(Person, pk=pk)
    status =request.GET.get('status')
    form.status= status
    form.published_date= timezone.now()
    if (form.status == 'accepted'):
        form.user.is_voter = False
    form.save()
    return redirect('accounts:dashboard')

def sdetails(request, pk):
    form = get_object_or_404(Person, pk=pk)
    return render(request,'accounts/sdetails.html', {'res': form})