"""finalproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('addAnimal/', addAnimal),
    path('logout/', logout),
    path('viewMessages/', viewMessages),
    path('sendMessage/message=<str:contents>', sendMessage),
    path('addlocation/', addlocation),
    path('listlocations/', listlocations),
    path('locationdetails/<int:id>/', locationDetails),
    path('', home),
    path('register/', registerUser),
    path('registervet/', registervet),
    path('verify/<str:username>/<dates>/', verifyUser),
    path('verifyVet/<str:username>/<dates>/', verifyVet),
    path('test/', test),
    path('login/', login),

    path('verify/<str:username>/<dates>/', verifyUser),
    path('verifyVet/<str:username>/<dates>/', verifyVet),
    path('emergency/', emergency),
    path('getVetFirstName/<str:vet_username>', getVetFirstName),




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
