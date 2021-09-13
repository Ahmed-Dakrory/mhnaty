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

from django.utils.translation import activate, get_language

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
    if request.method=='POST':
        firstNameData = request.POST['first_name']
        emailData = request.POST['email']
        passwordData = request.POST['password']
        roleId = 2
        regionData = request.POST['region']
        addressData = request.POST['address']
        phoneData = request.POST['phone']
        phone2Data = request.POST['phone2']
        usernameData = request.POST['username']
        typeOfRegisterationData = 0
        
        findLastUser = User.objects.filter(Q(email=emailData)|Q(username=usernameData))
        if roleId !='':
            roleData = role.objects.get(id=roleId)
        else:
            roleData = None


        regionData = region.objects.get(pk=region)
        

        if len(findLastUser) == 0:
            
            usernew = User.objects.create_user(username=usernameData,  password=passwordData,email=emailData,first_name=firstNameData,
            last_name='')
            usernew.save()

            dataToInsert = profile.objects.create(user=usernew,role=roleData,typeOfRegisteration=typeOfRegisterationData
            ,region=regionData,address=addressData
            ,phone=phoneData,mobile=phone2Data)
            dataToInsert.save()

            user = authenticate(username=usernameData, password=passwordData)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/'+get_language()+'/')

        


    return render(request,'index_reg.html',None)



def getlistOfcities(request):
    
    with connection.cursor() as cursorLast:
    
        try:
            sql_query = """

                    select concat('{"Result":"Ok","Number":',count(*),',"data":[',group_concat(concat('{"id":',x.id,',"name":"',x.name,'"}')),']}')
                    as output 
                    from (
                    SELECT  id,name FROM city
                    where deleted!=1
                    ) x;


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
            city = request.POST['city']
            
            if city !='':
                sql_query = """

                        select concat('{"Result":"Ok","Number":',count(*),',"data":[',group_concat(concat('{"id":',x.id,',"name":"',x.name,'"}')),']}')
                    as output 
                    from (
                    SELECT  region.id,region.name as name FROM region
                    left join city on city.id = region.cityOfRegion_id
                    where LOWER(city.name)=LOWER('"""+city+"""') ) x;



                    """
            else:
                sql_query = """

                         select concat('{"Result":"Ok","Number":',count(*),',"data":[',group_concat(concat('{"id":',x.id,',"name":"',x.name,'"}')),']}')
                    as output 
                    from (
                    SELECT  region.id,region.name as name FROM region
                    left join city on city.id = region.cityOfRegion_id
                    ) x;





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
    city = request.POST['city']
    region = request.POST['region']


    print(pageNumber)
    print(category)
    print(city)
    print(region)
    try:
        if searchKey == '':

            if category!='':
                categorySearch = Q(category__name__contains=category)
            else:
                categorySearch = Q(id__isnull=False)

            

            if city!='':
                citySearch = Q(owner__region__cityOfRegion__name__contains=city)
            else:
                citySearch = Q(id__isnull=False)

            if region!='':
                regionSearch =  Q(owner__region__name__contains=region)
            else:
                regionSearch = Q(id__isnull=False)

            allElements = theadd.objects.filter( Q(id__isnull=False)
            & (categorySearch
            & citySearch
            & regionSearch)
            & Q(deleted=False))

        else:
            allElements = theadd.objects.filter(Q(deleted=False) & 
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
        allElementsJson = {"draw": draw,"recordsTotal": len(allElements),"recordsFiltered": math.ceil(len(allElements)/pageLength),"data":[]}

        for result in listResult:
            allElementsJson['data'].append(result.to_json())

        return JsonResponse(allElementsJson)
    except Exception as e:
        print("Ahmed Error: "+str(e))
        return JsonResponse({"draw": draw,"recordsTotal": len(allElements),"recordsFiltered": math.ceil(len(allElements)/pageLength),"data":[]})


def SearchPage(request):
    allAdds = theadd.objects.filter(Q(deleted=False))

    allMainCategories = category.objects.filter(Q(deleted=False))

    data = {
        'allAdds':allAdds,
        'allMainCategories':allMainCategories
    }
    return render(request,'index_search.html',data)


@login_required
def profileWeb(request):
    user =request.user
    userobject = User.objects.filter(pk=user.id)
    userProfile = profile.objects.filter(user=user)

   


    if request.method=='POST':
        typeOfForm = request.POST['typeOfForm']  

        print(typeOfForm)
        if typeOfForm == 'mainData':
            nameData = request.POST['name'] 
            
            phoneData = request.POST['phone']
            addressData = request.POST['address']
            mobileData = request.POST['mobile'] 

            userobject.update(first_name=nameData)
            userProfile.update(phone=phoneData,mobile=mobileData,address=addressData)
        elif typeOfForm == 'mainImage':
            userProfile = profile.objects.get(user=user)
            userProfile.image = request.FILES['file-input']
            
            userProfile.save()

            
        
    return render(request,'profile.html',None)



def CompanyPage(request):
    id = request.GET['id']
    thisAdd = theadd.objects.get(pk=id)
    allFiles = thisAdd.images.all()
    allTags = thisAdd.owner.tags.all()
    numberOfFiles = len(allFiles)
    if len(allFiles) > 0: 
        mainImage = thisAdd.images.first
    else:
        mainImage=None


    allcomments = thisAdd.comments.all()
    user =request.user
    if user.is_authenticated:
        userProfile = profile.objects.get(user=user)
        if request.method=='POST':
            typeOfForm = request.POST['typeOfForm']
            if typeOfForm == 'feedBack':
                mainRateFromUser = request.POST['mainRateFromUser']
                subject = request.POST['subject']
                commentNew = comment.objects.create(fromUser=userProfile,details=subject,rate=mainRateFromUser)
                commentNew.save()
                thisAdd.comments.add(commentNew)

    

    data = {
        'allTags':allTags,
        'thisAdd':thisAdd,
        'rate':thisAdd.comments.aggregate(Avg('rate'))['rate__avg'],
        'allFiles':allFiles,
        'allcomments':allcomments,
        'mainImage':mainImage,
        'numberOfFiles':numberOfFiles
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

    allCategories = category.objects.filter(Q(deleted=False)&Q(name__contains=SearchQuery))

    allJson = []
    for item in list(allCategories):
        allJson.append({"value": item.id , "text": item.name   , "continent": item.name })

    
    return JsonResponse(allJson, safe=False)





def sendReply(request):

    commentid =request.POST['commentid'] 
    profileid =request.POST['profileid'] 
    replyDetails =request.POST['replyDetails'] 


    profileData = profile.objects.get(id=profileid)
    thiscomment = comment.objects.get(pk=commentid)
    dataReply = reply.objects.create(fromUser=profileData,  details=replyDetails)
    dataReply.save()
    thiscomment.replies.add(dataReply)
    
    listResult = reply.objects.filter(Q(deleted=False)&Q(comment__id=commentid))
    
    allJson = {'Result':'Ok','data':[]}

    for result in list(listResult):
        allJson['data'].append(result.to_json())
    # except:
    #     allJson = {'Result':'Error'}

    
    return JsonResponse(allJson, safe=False)


def getAllRepliesForComment(request):

    id =request.POST['id'] 

    listResult = reply.objects.filter(Q(deleted=False)&Q(comment__id=id))
    
    allJson = {'Result':'Ok','data':[]}

    for result in list(listResult):
        allJson['data'].append(result.to_json())
    # except:
    #     allJson = {'Result':'Error'}

    
    return JsonResponse(allJson, safe=False)

def getAllExperiansesJson(request):
    SearchQuery =request.GET['query'] 

    allCategories = category.objects.filter(Q(deleted=False)&Q(name__contains=SearchQuery))

    allJson = []
    for item in list(allCategories):
        allJson.append({"value": item.id , "text": item.name   , "continent": item.name })

    
    return JsonResponse(allJson, safe=False)



def AuthOutSide(request):
    
    try:
        firstNameData = request.POST['firstName']
        lastNameData = request.POST['lastName']
        emailData = request.POST['email']
        passwordData = request.POST['email']+str('AhmedAuth')
        roleId = request.POST['role']
        img_url = request.POST['img']
        usernameData = request.POST['username']
        typeOfRegisterationData = request.POST['typeOfRegisteration']
        
        findLastUser = User.objects.filter(Q(email=emailData)|Q(username=usernameData))
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
            
            dataToInsert = profile.objects.create(user=usernew,role=roleData,image=img_temp,typeOfRegisteration=typeOfRegisterationData)
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
            # user = authenticate(username=usernameData, password=passwordData)
            user = User.objects.get(email=emailData)
            print(user)
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
                    'Error':'Registered Email or username',
                    'RedirectUrl':'/'
                    }


                
            

        
    except Exception as e:
        response = {
                'State':'Error',
                'statment':str(e)
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




def checkusername(request):
       
    try:
        usernameData = request.POST['username']
        
        user = User.objects.filter(username=usernameData)

        if len(user)>0:
            response = {
                'State':'Ok',
                'statment':'Exists'
            }
        else:
            response = {
                'State':'Ok',
                'statment':'NotExists'
            }


    
    except Exception as e:
        response = {
                'State':'Error',
                'statment':str(e)
            }
    
    return JsonResponse(response, safe=False)


def checkemail(request):
    
    try:
        emailData = request.POST['email']
        
        user = User.objects.filter(email=emailData)

        if len(user)>0:
            response = {
                'State':'Ok',
                'statment':'Exists'
            }
        else:
            response = {
                'State':'Ok',
                'statment':'NotExists'
            }


    
    except Exception as e:
        response = {
                'State':'Error',
                'statment':str(e)
            }
    
    return JsonResponse(response, safe=False)