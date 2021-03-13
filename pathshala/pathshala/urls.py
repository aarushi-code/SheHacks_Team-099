"""e-Pathchala URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    #path('auth/', include('djoser.urls')),
    path('admin/', admin.site.urls),
    path('chat/', include('chatapp.urls')),
    path('core/', include('core.urls')), 
    #path('threaded_messages/', include('threaded_messages.urls')), 
    path('msat/', include('msat.urls')), 
    path('login/',views.loginPage,name="loginPage"),
    path('SignUp/',views.SignUp,name="SignUp"),
    path('questionUpload/',views.questionUpload,name="questionUpload"),
    path('account/', views.accountPage, name="account"),
    path('logout/', views.logoutUser, name="logout"),
    path('handle_login/', views.handle_login, name="handle_login"),
    path('', views.landing, name="landing"),
    path('about/', views.about, name="about"),
    path('profile/', views.update , name="eprofil"),
    path('contactus/', views.contact, name="contact"),
    path('coursepage/', views.coursePage, name="coursepage"),
    path('pricing/', views.pricing, name="pricing"),
    path('additional_details/', views.additional_details, name="additional_details"),
    path('landing_final/',views.landing_final,name="landing_final"),
    path('features/',views.features,name="features"),
    path('faq_page/',views.faq_page,name="faq_page"),
    path('cart/',views.cart,name="cart"),
    path('card/',views.card,name="card"),
    
    path('accounts/', include('allauth.urls')),
    path('accounts/google/login/callback/dashboard/',views.dashboard,name="dashboard"),

    path('paypal/', include('paypal.standard.ipn.urls')),

    # For email verification link-
    #re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #    views.activate, name='activate'),

    path('dashboard/',views.dashboard,name="dashboard"),
    path('login/password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='password_reset.html'),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='password_reset_sent.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='password_reset_form.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='password_reset_done.html'
         ),
         name='password_reset_complete'),

    #path('checkout/', views.checkout, name='checkout'),
    #path('process-payment/', views.process_payment, name='process_payment'),
    #path('payment-done/', views.payment_done, name='payment_done'),
    #path('payment-cancelled/', views.payment_canceled, name='payment_cancelled'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)