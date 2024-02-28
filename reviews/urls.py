from django.conf import *
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns=[
    path('review',review_list,name='review_list'),
    path('add/', add_reviews, name='add_review'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)