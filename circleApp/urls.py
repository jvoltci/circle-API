from django.conf.urls import url
from circleApp import views


urlpatterns = [
    url(r'^product$', views.productApi),
    url(r'^product/category/([0-9]+)$', views.productCategoryApi),
    url(r'^product/subcategory/([0-9]+)$', views.productSubCategoryApi),
    url(r'^category$', views.categoryApi),
    url(r'^category/([0-9]+)$', views.categoryApi),
]