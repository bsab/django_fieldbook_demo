"""django_fieldbook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

from app import forms
from app.views import IndexView, UserRegistrationView, SheetTableView, SheetEntryView
from app.views import webhook

urlpatterns = [

    url('^$', IndexView.as_view(), name="index"),
    url(r'^webhook', webhook, name='webhook'),#to remove

    url(r'^login/$', auth_views.login,
        {'template_name': 'login.html',
         'authentication_form': forms.MaterialLoginForm},
        name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
    url(r'^register/$', UserRegistrationView.as_view(), name="registration"),
    url(r'^help/$', TemplateView.as_view(template_name="help.html"), name="help"),

    # list sheets
    url(r'^sheet-table/sheet_name=(?P<sheet_name>[-\w]+)/$', SheetTableView.as_view(), name='sheet_table'),
    # single sheet by id
    url(r'^sheet-entry-(?P<record_id>\w+)/sheet_name=(?P<sheet_name>[-\w]+)/$', SheetEntryView.as_view(),
        name='sheet_entry'),
    url(r'^sheet-entry-(?P<record_id>\w+)/sheet_name=(?P<sheet_name>[-\w]+)/delete/$', SheetEntryView.as_view(),
        {'to_delete': True}, name='sheet_entry_delete'),

]
