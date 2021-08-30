from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import permission_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.views.decorators.csrf import csrf_protect
from datetime import datetime, timedelta,date,time



from django.shortcuts import get_object_or_404
from django.http import Http404
from django.core.exceptions import SuspiciousOperation
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
import json
from django.db.models import Q
from django.shortcuts import render

from .models import *
# Create your views here.



def customError400(request, exception):
    return render(request, '400.html')


def customError404(request, exception):
    return render(request, '404.html')


def customError500(request):
    return redirect('http://www.onlydispatch.com')
    
def logout_req(request):
    logout(request)
    return redirect(request.META['HTTP_REFERER'])

def authUser(request):
    
    try:
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            allJson={'Result':'Success','url':request.META['HTTP_REFERER']}
            # Redirect to a success page.
        else:
            allJson={'Result':'Fail'}
            # Return an 'invalid login' error message.
            print("invalid")
    except:
        allJson={'Result':'Fail'}
    
    return JsonResponse(allJson, safe=False)




def loadLoginPage(request):
    
    return render(request,'index_login.html',None)


def loadRegPage(request):
    return render(request,'index_reg.html',None)


def getNewResultsForAds(request):
    print('---------------------------------------------------')
    print(request.POST)
    print(request.GET)
    print('---------------------------------------------------')
    pageLength = int(request.POST['length'])
    pageNumber = int(request.POST['start'])
    draw = int(request.POST['draw'])
    searchKey = request.POST['search[value]']
    pageNumber = int(pageNumber/pageLength + 1)
    
    try:
        if searchKey == '':
            allElements = theAdd.objects.filter( Q(id__isnull=False) & Q(deleted=False))
        else:
            allElements = theAdd.objects.filter(Q(deleted=False) & 
            (Q(name__contains=searchKey) |
             Q(details__contains=searchKey) |
             Q(category__name__contains=searchKey) ))


        if pageLength == -1:
            if allElements !=None:
                pageLength = len(allElements)

        paginator = Paginator(allElements, pageLength)
        
        try:
            response = paginator.page(pageNumber)
        except PageNotAnInteger:
            response = paginator.page(pageNumber)
        except EmptyPage:
            response = paginator.page(paginator.num_pages)

        listResult = list(response)
        allElementsJson = {"draw": draw,"recordsTotal": len(allElements),"recordsFiltered": len(allElements)/pageLength+1,"data":[]}

        for result in listResult:
            allElementsJson['data'].append(result.to_json())

        return JsonResponse(allElementsJson)
    except Exception as e:
        print("Ahmed Error: "+str(e))
        return JsonResponse({"draw": draw,"recordsTotal": len(allElements),"recordsFiltered": len(allElements)/pageLength+1,"data":[]})


def SearchPage(request):
    allAdds = theAdd.objects.filter(Q(deleted=False))

    allMainCategories = category.objects.filter(Q(deleted=False))

    data = {
        'allAdds':allAdds,
        'allMainCategories':allMainCategories
    }
    return render(request,'index_search.html',data)

def CompanyPage(request):
    thisAdd = theAdd.objects.get(pk=1)
    allFiles = thisAdd.images.all()

    data = {
        'thisAdd':thisAdd,
        'allFiles':allFiles
    }

    return render(request,'index_company.html',data)


def loadMainPage(request):

    allMainCategories = category.objects.filter(Q(deleted=False))

    data = {
        'allMainCategories':allMainCategories
    }
    return render(request,'index.html',data)

def getAllCategoriesJson(request):
    SearchQuery =request.GET['query'] 

    print('-----------------------------------------------------------')
    print(SearchQuery)
    allJson=[ { "value": 1 , "text": "أحمد"   , "continent": "أحمد"    },
            { "value": 2 , "text": "محمد"      , "continent": "محمد"    },
            { "value": 3 , "text": "سيد"       , "continent": "سيد"    },
            { "value": 4 , "text": "عباس"  , "continent": "عباس"   },
            { "value": 5 , "text": "محمود" , "continent": "محمود"   },
            { "value": 6 , "text": "متعب", "continent": "متعب"   },
            { "value": 7 , "text": "فؤاد"      , "continent": "فؤاد" },
            { "value": 8 , "text": "يوسف"  , "continent": "يوسف" },
            { "value": 9 , "text": "عبدالرحمن"    , "continent": "عبدالرحمن" },
            { "value": 10, "text": "معروف"     , "continent": "معروف"      }
            ]
    # allJson = [ { "value": 1 , "text": "Amsterdam"   , "continent": "Europe"    },
    #             { "value": 2 , "text": "London"      , "continent": "Europe"    },
    #             { "value": 3 , "text": "Paris"       , "continent": "Europe"    },
    #             { "value": 4 , "text": "Washington"  , "continent": "America"   },
    #             { "value": 5 , "text": "Mexico City" , "continent": "America"   },
    #             { "value": 6 , "text": "Buenos Aires", "continent": "America"   },
    #             { "value": 7 , "text": "Sydney"      , "continent": "Australia" },
    #             { "value": 8 , "text": "Wellington"  , "continent": "Australia" },
    #             { "value": 9 , "text": "Canberra"    , "continent": "Australia" },
    #             { "value": 10, "text": "Beijing"     , "continent": "Asia"      },
    #             { "value": 11, "text": "New Delhi"   , "continent": "Asia"      },
    #             { "value": 12, "text": "Kathmandu"   , "continent": "Asia"      },
    #             { "value": 13, "text": "Cairo"       , "continent": "Africa"    },
    #             { "value": 14, "text": "Cape Town"   , "continent": "Africa"    },
    #             { "value": 15, "text": "Kinshasa"    , "continent": "Africa"    }
    #             ]
    
    return JsonResponse(allJson, safe=False)