from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from student.forms import UserForm,LoginForm
from django.contrib.auth import authenticate,logout,get_user_model
from django.contrib.auth import authenticate,login 
from django.contrib.auth.decorators import login_required
from student_management.decorators import admin_only
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView 
from django.contrib import auth
from django.views.generic import TemplateView


def user_logout(request):
	if request.method == 'POST':
		logout(request)
		return HttpResponseRedirect(reverse('login'))

@login_required(login_url='/login/')
def success(request):
	context = {}
	context['user'] = request.user
	return render(request,'auth/success.html',context)

@login_required(login_url='/login/')
def student_list(request):
	context = {}
	context['users'] = User.objects.all()
	context['title'] = 'Students'
	return render(request,"student/index.html",context)

@login_required(login_url='/login/')
def student_details(request,id=None):
	user = get_object_or_404(User,id=id)
	user_form = UserForm(instance=user)
	return render(request,'student/details.html', {'user_form':user_form})

@login_required(login_url='/login/')
# @admin_only	
def student_add(request,id=None):
	context = {}
	if request.method == 'POST':
		user_form = UserForm(request.POST)
		if user_form.is_valid():
			user_form.save()
			return HttpResponseRedirect(reverse('student_list'))
		else:
			return render(request,'student/add.html', {'user_form':user_form})
	else:
		user_form = UserForm()
		return render(request,'student/add.html',{'user_form':user_form})

@login_required(login_url='/login/')
def student_edit(request,id=None):
	user = get_object_or_404(User,id=id)
	if request.method == 'POST':
		user_form = UserForm(request.POST,instance=user)
		if user_form.is_valid():
			user_form.save()
			return HttpResponseRedirect(reverse('student_list'))
		else:
			return render(request,'student/edit.html', {'user_form':user_form})
	else: 
		user_form = UserForm(instance=user)
		return render(request,'student/edit.html',{'user_form':user_form})

@login_required(login_url='/login/')
def student_delete(request,id=None):
	user = get_object_or_404(User,id=id)
	if request.method == 'POST':
		user.delete()
		return HttpResponseRedirect(reverse('student_list'))
	else:
		context = {}
		context['user'] = user
		return render(request,'student/delete.html',context)

class ProfileUpdate(UpdateView):
	fields = ['designation','salary']
	template_name = 'auth/profile_update.html'
	success_url = reverse_lazy('my_profile')

	def get_object(self):
		return self.request.user.profile

class MyProfile(DetailView):
	template_name = 'auth/profile.html'

	def get_object(self):
		return self.request.user.profile

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        'form': form
    }
    print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/student/')
        else:
            print("error.......")

    return render(request, "auth/login.html", context=context)

def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()

			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('home')
	else:
			form = UserCreationForm()

	context = {'form':form}
	return render(request,'auth/register.html',context)

def home(request):
	return render(request,'index.html')