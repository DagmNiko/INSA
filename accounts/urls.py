from django.urls import path

from accounts.views import AccountSignIn

urlpatterns = [
    path('signin', AccountSignIn, name='signin'),
]
