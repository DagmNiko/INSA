from django.shortcuts import render, redirect
from django.views import generic

from accounts.models import Account
from .forms import AccountCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.backends import BaseBackend
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserChangeForm
from django.views import generic



class AccountEditView(generic.UpdateView):
	form_class = UserChangeForm
	template_name = 'editProfilePage.html'

	def get_success_url(self):
		return reverse_lazy('profile-page', kwargs={'usr':self.kwargs['usr']})
	def get_object(self):
		return Account.objects.get(username=self.kwargs['usr'])
	
	
def ProfilePageView(request, usr):
	acc = Account.objects.get(username=usr)
	if request.method == 'POST':
		current_account = request.user
		action = request.POST['follow']
		if action == 'follow':
			current_account.follows.add(acc)
		else:
			current_account.follows.remove(acc)

		
	return render(request, 'profilePage.html', {'acc': acc})

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
