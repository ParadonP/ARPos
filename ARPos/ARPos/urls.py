"""ARPos URL Configuration

accounts/ view has the following
accounts/login/ [name='login']
accounts/logout/ [name='logout']
accounts/password_change/ [name='password_change']
accounts/password_change/done/ [name='password_change_done']
accounts/password_reset/ [name='password_reset']
accounts/password_reset/done/ [name='password_reset_done']
accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
accounts/reset/done/ [name='password_reset_complete']
"""
from django.contrib import admin
from django.urls import include, path
from cashregister import views as crviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inventory/', include('inventory.urls')),
    path('cashregister/', include('cashregister.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', crviews.index, name='index'),
]
