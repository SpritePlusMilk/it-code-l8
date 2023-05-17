from django.urls import path
from core import views


app_name = 'core'

urlpatterns =[
    path('',views.index, name='main_page'),
    path('cl_list', views.ClientsList.as_view(), name='cl_list'),
    path('client/<int:pk>', views.DetailClient.as_view(), name='detail_cl'),
    path('websites',views.WebsitesList.as_view(), name='ws_list'),
    path('website/<int:pk>',views.DetailWebsite.as_view(), name='detail_ws')
]