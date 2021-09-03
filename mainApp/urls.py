from django.urls import path
from . import views 

app_name = 'mainApp'



urlpatterns = [
    path('',views.loadMainPage,name = 'loadMainPage'),
    path('SearchPage/',views.SearchPage,name = 'SearchPage'),
    path('CompanyPage/',views.CompanyPage,name = 'CompanyPage'),
    path('profile/',views.profileWeb,name = 'profileWeb'),
    path('accounts/login/',views.loadLoginPage,name = 'loadLoginPage'),
    path('loadRegPage/',views.loadRegPage,name = 'loadRegPage'),
    path('getAllCategoriesJson.json',views.getAllCategoriesJson,name = 'getAllCategoriesJson'),
    path('getNewResultsForAds',views.getNewResultsForAds,name = 'getNewResultsForAds'),
    path('AuthOutSide',views.AuthOutSide,name = 'AuthOutSide'),
    path('getServiceProviders',views.getServiceProviders,name = 'getServiceProviders'),
    path('getListOfRegions',views.getListOfRegions,name = 'getListOfRegions'),
    path('getListOfCountries',views.getListOfCountries,name = 'getListOfCountries'),
    


 
    
    # path('print/<username>/', views.print_from_button ,name='printButton'),
    # path('ajax', views.answer_me, name='get_response'),
    path('authUser', views.authUser, name='authUser'),
    path('logout/', views.logout_req, name='logout'),
    # path('logoutSecured', views.logoutSecured_req, name='logoutSecured'),
]
