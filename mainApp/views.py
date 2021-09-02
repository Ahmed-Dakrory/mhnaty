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
import urllib.request
from django.core.files.uploadedfile import SimpleUploadedFile
import uuid
from django.shortcuts import HttpResponseRedirect   
from django.http import HttpResponse
from django.db import connection
import math
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


def getServiceProviders(request):
    
    with connection.cursor() as cursorLast:
    
        try:
            category = request.POST['category']
            
            if category !='':
                sql_query = """

                        select concat('{"Result":"Ok","Number":',count(*),',"data":[',group_concat(concat('{"id":',x.id,',"name":"',x.name,'"}')),']}')
                        as output 
                        from (
                        SELECT  profile.id,auth_user.first_name as name FROM theadd
                        left join profile on profile.id = theadd.owner_id
                        left join auth_user on profile.user_id = auth_user.id
                        left join category on category.id = theadd.category_id
                        where category.name = '"""+str(category)+"""' and auth_user.first_name !='' and auth_user.first_name !=' '
                        group by profile.id) x;



                    """
            else:
                sql_query = """

                        select concat('{"Result":"Ok","Number":',count(*),',"data":[',group_concat(concat('{"id":',x.id,',"name":"',x.name,'"}')),']}')
                        as output 
                        from (
                        SELECT  profile.id,auth_user.first_name as name FROM theadd
                        left join profile on profile.id = theadd.owner_id
                        left join auth_user on profile.user_id = auth_user.id
                         where  auth_user.first_name !='' and auth_user.first_name !=' '
                        group by profile.id) x;



                    """


            cursorLast.execute(sql_query)
            cursorAllData = cursorLast.fetchone()
            y=cursorAllData[0].replace('\r\n','')
            # print(y)
            return HttpResponse(y,content_type='application/json')
        except Exception as e:
            print(e)
            allJson = {"Result": "Fail"}
            return JsonResponse(allJson, safe=False)



def getListOfCountries(request):
    
    with connection.cursor() as cursorLast:
    
        try:
            sql_query = """

                    select concat('{"Result":"Ok","Number":',count(*),',"data":[',group_concat(concat('{"id":',x.id,',"name":"',x.name,'"}')),']}')
                    as output 
                    from (
                    SELECT  profile.id,profile.country as name FROM theadd
                    left join profile on profile.id = theadd.owner_id
                    where profile.country !='' and profile.country !=' '
                    group by profile.country) x;


                """
            

            cursorLast.execute(sql_query)
            cursorAllData = cursorLast.fetchone()
            y=cursorAllData[0].replace('\r\n','')
            # print(y)
            return HttpResponse(y,content_type='application/json')
        except Exception as e:
            print(e)
            allJson = {"Result": "Fail"}
            return JsonResponse(allJson, safe=False)




def getListOfRegions(request):
    
    with connection.cursor() as cursorLast:
    
        try:
            country = request.POST['country']
            
            if country !='':
                sql_query = """

                        select concat('{"Result":"Ok","Number":',count(*),',"data":[',group_concat(concat('{"id":',x.id,',"name":"',x.name,'"}')),']}')
                    as output 
                    from (
                    SELECT  profile.id,profile.region as name FROM theadd
                    left join profile on profile.id = theadd.owner_id
                    where LOWER(profile.country)=LOWER('"""+country+"""') and profile.region !='' and profile.region !=' '
                    group by profile.region) x;



                    """
            else:
                sql_query = """

                        select concat('{"Result":"Ok","Number":',count(*),',"data":[',group_concat(concat('{"id":',x.id,',"name":"',x.name,'"}')),']}')
                    as output 
                    from (
                    SELECT  profile.id,profile.region as name FROM theadd
                    left join profile on profile.id = theadd.owner_id
                    where  profile.region !='' and profile.region !=' '
                    group by profile.region) x;




                    """


            cursorLast.execute(sql_query)
            cursorAllData = cursorLast.fetchone()
            y=cursorAllData[0].replace('\r\n','')
            # print(y)
            return HttpResponse(y,content_type='application/json')
        except Exception as e:
            print(e)
            allJson = {"Result": "Fail"}
            return JsonResponse(allJson, safe=False)

       





def getNewResultsForAds(request):
    pageLength = int(request.POST['length'])
    pageNumber = int(request.POST['start'])
    draw = int(request.POST['draw'])
    searchKey = request.POST['search[value]']
    pageNumber = int(pageNumber/pageLength + 1)
    

    category = request.POST['category']
    provider = request.POST['provider']
    country = request.POST['country']
    region = request.POST['region']

    try:
        if searchKey == '':
            allElements = theAdd.objects.filter( Q(id__isnull=False)
            & Q(category__name__contains=category)
            & Q(owner__user__first_name__contains=provider)
            & Q(owner__country__contains=country)
            & Q(owner__region__contains=region)
            & Q(deleted=False))
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
        allElementsJson = {"draw": draw,"recordsTotal": len(allElements),"recordsFiltered": math.ceil(len(allElements)/pageLength)-1,"data":[]}

        for result in listResult:
            allElementsJson['data'].append(result.to_json())

        return JsonResponse(allElementsJson)
    except Exception as e:
        print("Ahmed Error: "+str(e))
        return JsonResponse({"draw": draw,"recordsTotal": len(allElements),"recordsFiltered": math.ceil(len(allElements)/pageLength)-1,"data":[]})


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



def AuthOutSide(request):
    
    try:
        firstNameData = request.POST['firstName']
        lastNameData = request.POST['lastName']
        emailData = request.POST['email']
        passwordData = request.POST['email']+str('AhmedAuth')
        roleId = request.POST['role']
        img_url = request.POST['img']
        usernameData = request.POST['email']
        
        findLastUser = User.objects.filter(email=emailData)
        if roleId !='':
            roleData = role.objects.get(id=roleId)
        else:
            roleData = None

        if len(findLastUser) == 0:
            
            usernew = User.objects.create_user(username=usernameData,  password=passwordData,email=emailData,first_name=firstNameData,
            last_name=lastNameData)
            usernew.save()

            basename = str(uuid.uuid1())+'jpg'
            tmpfile, _ = urllib.request.urlretrieve(img_url)
            img_temp = SimpleUploadedFile(basename, open(tmpfile, "rb").read())
            
            dataToInsert = profile.objects.create(user=usernew,role=roleData,image=img_temp)
            dataToInsert.save()
            user = authenticate(username=usernameData, password=passwordData)
            if user is not None:
                login(request, user)

            response = {
                'State':'Ok',
                'isExist':'No',
                'ableToLogin':'Yes',
                'RedirectUrl':'/'
            }
        else:
            user = authenticate(username=usernameData, password=passwordData)
            if user is not None:
                login(request, user)
                response = {
                    'State':'Ok',
                    'isExist':'Ok',
                    'ableToLogin':'Yes',
                    'RedirectUrl':'/'
                    }
            else:
                response = {
                    'State':'Ok',
                    'isExist':'Ok',
                    'ableToLogin':'No',
                    'Error':'Registered Email',
                    'RedirectUrl':'/'
                    }


                
            

        
    except:
        response = {
                'State':'Error'
            }
    
    return JsonResponse(response, safe=False)



def addnew_profile(request):
    all_role = role.objects.all()
    all_job = job.objects.all()
    typeOfEntry = request.GET['type']
    if typeOfEntry == 'new':
        dataToInsert = None
    elif typeOfEntry == 'edit':
        idOfelement = request.GET['id']
        dataToInsert = profile.objects.get(id=idOfelement)
    
    
    context = {
        'all_role':all_role,
        'all_job':all_job,
        'profileData':dataToInsert,
        'type':typeOfEntry}

    if request.method=='POST':
        emailData = request.POST['email']
        passwordData = request.POST['password']
        addressData = request.POST['address']
        phoneData = request.POST['phone']
        roleId = request.POST['role']
        jobId = request.POST['job']
        
        if jobId !='':
            jobData = job.objects.get(id=jobId)
        else:
            jobData = None

        if roleId !='':
            roleData = role.objects.get(id=roleId)
        else:
            roleData = None

        if typeOfEntry == 'new':
            usernameData = request.POST['username']
            usernew = User.objects.create_user(username=usernameData,  password=passwordData,email=emailData)
            usernew.save()

            dataToInsert = profile.objects.create(user=usernew,job=jobData,address=addressData,phone=phoneData,role=roleData)
            dataToInsert.save()
        elif typeOfEntry == 'edit':
            dataToInsert = profile.objects.filter(id=idOfelement)
            userData = profile.objects.get(pk = idOfelement).user
            if passwordData!='':
                userData.set_password(passwordData)
                userData.save()
            
            User.objects.filter(id=userData.id).update(email=emailData)
            dataToInsert.update(address=addressData,job=jobData,phone=phoneData,role=roleData)
            


        return HttpResponseRedirect('/'+get_language()+'/listOf_profile')
    elif request.method=='GET':
        return render(request,'controls/users/profile/addnew.html',context)
