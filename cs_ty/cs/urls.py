from django.urls import path
from . import views
from django.urls import register_converter
from .converters import YearConverter

register_converter(YearConverter, 'year')

urlpatterns = [
    path('', views.index, name='home'),
    path('category/<int:cat_id>/', views.category, name='category_id'),
    path('category/<slug:cat_slug>/', views.category_slug, name='category_slug'),
    path('archive/<year:year>/', views.archive, name='archive'),
]

handler404 = 'cs.views.custom_404'