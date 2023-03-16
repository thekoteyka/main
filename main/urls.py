"""main URL Configuration

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
from django.urls import path
from rating.views import SimpleFormView
from rating.views import RatingListView, RatingEntryListView, RatingsDetailView, RatingDetailView
from registration.views import RegistrationView, LoginView, ProfileView
from pagination_example.views import pagination_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', SimpleView.as_view()),
    path('', RatingListView.as_view(), name='main'),
    path('form/', SimpleFormView.as_view()),
    path('entry/<name>/', RatingEntryListView.as_view()),
    path('rating/<int:pk>', RatingDetailView.as_view()),
    path('register/', RegistrationView.as_view()),
    path('login/', LoginView.as_view(), name='login'),
    path('accounts/profile/', ProfileView.as_view()),
    path('pagination_example/', pagination_view)
]
