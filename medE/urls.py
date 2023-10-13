"""
URL configuration for medE project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
from Home import views as  firstactivity
from products import views as  secondactivity
from django.conf import settings
from django.conf.urls.static import static

from authentication import views as authenticationViews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',firstactivity.home, name='home'),
    path('product/<str:p_name>/', secondactivity.prod, name='prod'),
    path("Category<str:p_category>/",secondactivity.category,name='category'),
    path('live_search/', secondactivity.live_search, name='live_search'),
    path('get_product_info/<int:p_id>/', secondactivity.get_product_info, name='get_product_info'),
    path('send_otp/', authenticationViews.send_otp, name='send_otp'),
    path('verify_otp/', authenticationViews.verify_otp, name='verify_otp'),
    path('login/', authenticationViews.mylogin, name='mylogin'),
    path('register/', authenticationViews.myregister, name='myregister'),
    path('logout/', authenticationViews.mylogout, name='mylogout'),
    path('profile/',firstactivity.profile, name='profile'),
    path('profile/update_profile/', authenticationViews.update_profile, name='update_profile'),


    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)