from django.shortcuts import render, redirect
from django.views import generic
from .forms import AccountCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.backends import BaseBackend
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth import login, authenticate



def AccountSignIn(request, *args, **kwargs):
	user = request.user
	if user.is_authenticated: 
		return HttpResponse("You are already authenticated as " + str(user.email))

	context = {}
	if request.POST:
		form = AccountCreationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email').lower()
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(email=email, password=raw_password)
			login(request, account)

			return redirect('home')
		else:
			context['form'] = form

	else:
		form = AccountCreationForm()
		context['form'] = form
	return render(request, 'signin.html', context)
