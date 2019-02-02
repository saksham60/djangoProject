from django.contrib import admin
from django.urls import path,include,re_path
from basic_app import views

app_name='basic_app'

urlpatterns = [
    path('',views.SchoolListView.as_view(),name='list'),
#super imp as this is linking to students data through school so pk is for primary key
    re_path(r'^(?P<pk>[-\w]+)/$',views.SchoolDetailView.as_view(),name='detail'),
    path('creat',views.SchoolCreateView.as_view(),name='create'),
    re_path(r'^update/(?P<pk>[-\w]+)/$',views.SchoolUpdateView.as_view(),name='update'),
    re_path(r'^delete/(?P<pk>[-\w]+)/$',views.SchoolDeleteView.as_view(),name='delete'),

]
