from django.urls import path
from . import views 

app_name = 'mainApp'



urlpatterns = [
    path('',views.loadMainPage,name = 'loadMainPage'),
    path('SearchPage/',views.SearchPage,name = 'SearchPage'),
    path('CompanyPage/',views.CompanyPage,name = 'CompanyPage'),
    path('dashboard_add_listing/',views.dashboard_add_listing,name = 'dashboard_add_listing'),
    path('dashboard_messages/',views.dashboard_messages,name = 'dashboard_messages'),
    path('profile/',views.profile_main,name = 'profileWeb'),
    path('accounts/login/',views.loadLoginPage,name = 'loadLoginPage'),
    path('loadRegPage/',views.loadRegPage,name = 'loadRegPage'),
    path('getAllCategoriesJson',views.getAllCategoriesJson,name = 'getAllCategoriesJson'),
    path('getAllExperiansesJson',views.getAllExperiansesJson,name = 'getAllExperiansesJson'),
    path('getAllTagsJson',views.getAllTagsJson,name = 'getAllTagsJson'),


    
    path('getAllRepliesForComment',views.getAllRepliesForComment,name = 'getAllRepliesForComment'),
    path('sendReply',views.sendReply,name = 'sendReply'),
    path('controlpanel/',views.controlpanel,name='controlpanel'),
    path('uploadFiles_ForAdd',views.uploadFiles_ForAdd,name = 'uploadFiles_ForAdd'),
    path('getNewResultsForAds',views.getNewResultsForAds,name = 'getNewResultsForAds'),
    path('AuthOutSide',views.AuthOutSide,name = 'AuthOutSide'),
    path('getListOfcategoriesByparentOneId',views.getListOfcategoriesByparentOneId,name = 'getListOfcategoriesByparentOneId'),
    path('getAllAdsByCategoriesJson',views.getAllAdsByCategoriesJson,name = 'getAllAdsByCategoriesJson'),
    path('getListOfRegions',views.getListOfRegions,name = 'getListOfRegions'),
    path('getListOfRegionsByCityId',views.getListOfRegionsByCityId,name = 'getListOfRegionsByCityId'),
    path('getlistOfcities',views.getlistOfcities,name = 'getlistOfcities'),
    path('checkemail',views.checkemail,name = 'checkemail'),
    path('checkusername',views.checkusername,name = 'checkusername'),
    path('activation',views.activation,name = 'activation'),
    path('showUserMessages/<int:id>/',views.showUserMessages,name = 'showUserMessages'),
    path('activateNow/<str:token>/',views.activateNow,name = 'activateNow'),
    path('getProfileMessages',views.getProfileMessages,name = 'getProfileMessages'),
    path('sendMessage',views.sendMessage,name = 'sendMessage'),
    path('sendMessageToTheAdd',views.sendMessageToTheAdd,name='sendMessageToTheAdd'),
    


 
    
    # path('print/<username>/', views.print_from_button ,name='printButton'),
    # path('ajax', views.answer_me, name='get_response'),
    path('authUser', views.authUser, name='authUser'),
    path('logout/', views.logout_req, name='logout'),
    # path('logoutSecured', views.logoutSecured_req, name='logoutSecured'),
]
