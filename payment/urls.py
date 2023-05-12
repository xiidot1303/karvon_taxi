from django.urls import path, re_path
from django.contrib.auth.views import (
    LoginView, 
    LogoutView, 
    PasswordChangeDoneView, 
    PasswordChangeView
)

from payment.views import (
    click
)

urlpatterns = [
    # click endpoints
    path('click/get-info', click.send_profile_info),
]
