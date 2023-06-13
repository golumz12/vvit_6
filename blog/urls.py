"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, re_path
from blog import settings
from articles import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.archive),
    re_path(r'^article/(?P<article_id>\d+)$',
            views.get_article, name='get_article'),
    path('article/new', views.create_article, name='create_article'),
    path('admin/', admin.site.urls),
    path('register/', views.sign_up_user, name='sign_up_user'),
    path('login/', views.sign_in_user, name='sign_in_user'),
    path('logout/', views.sign_out_user, name='sign_out_user'),
] + static(settings.STATIC_URL)
