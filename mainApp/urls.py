from django.urls import path
from . import views 

app_name = 'mainApp'



urlpatterns = [
    path('',views.loadMainPage,name = 'loadMainPage'),
    path('SearchPage/',views.SearchPage,name = 'SearchPage'),
    path('CompanyPage/',views.CompanyPage,name = 'CompanyPage'),
    path('accounts/login/',views.loadLoginPage,name = 'loadLoginPage'),
    path('loadRegPage/',views.loadRegPage,name = 'loadRegPage'),
    path('getAllCategoriesJson.json',views.getAllCategoriesJson,name = 'getAllCategoriesJson'),
    path('getNewResultsForAds',views.getNewResultsForAds,name = 'getNewResultsForAds'),


 
    
    # path('print/<username>/', views.print_from_button ,name='printButton'),
    # path('ajax', views.answer_me, name='get_response'),
    path('authUser', views.authUser, name='authUser'),
    path('logout/', views.logout_req, name='logout'),
    # path('logoutSecured', views.logoutSecured_req, name='logoutSecured'),
]
