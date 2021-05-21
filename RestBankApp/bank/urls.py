"""RestBankApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .views import UserDetailsMixin, UserLogin, LogoutApi, BankAccountApi, WithdrawApi, DepositApi, BalanceApi,TransactionApi

urlpatterns = [
    path('register/',UserDetailsMixin.as_view()),
    path('login/',UserLogin.as_view()),
    path('logout/',LogoutApi.as_view()),
    path('create-account/', BankAccountApi.as_view()),
    path('balance/<int:account_number>', BalanceApi.as_view()),
    path('withdraw/<int:account_number>', WithdrawApi.as_view()),
    path('deposit/<int:account_number>', DepositApi.as_view()),
    path('send-money/', TransactionApi.as_view()),
    path('view-transactions/<int:account_number>', TransactionApi.as_view()),

    ]