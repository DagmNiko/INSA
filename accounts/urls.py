from django.urls import path

from accounts.views import *

urlpatterns = [
    path('signin', AccountSignIn, name='signin'),
    path('profile/<str:usr>', ProfilePageView, name='profile-page'),
    path('profile/<str:usr>/edit', AccountEditView.as_view(), name='profile-page-edit'),
]
