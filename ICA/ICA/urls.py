from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('Main.urls','Main'), namespace="Main")),
    path('', include(('Supplementary.urls','Supplementary'), namespace="Supp")),
]
