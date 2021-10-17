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


from django.core.files.storage import default_storage
from uuid import uuid4
import os
from django.http import HttpResponse
from django.core.files import File
from django.conf import settings
import mimetypes

from django.db.models import F, Func
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
from django.db import connection
import math

from django.utils.translation import activate, get_language
from django.db.models import Count
from .models import *
# Create your views here.

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six

# send email
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode



class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.is_active)
        )
account_activation_token = TokenGenerator()




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
    allCities = city.objects.filter(Q(deleted=False))
    if request.method=='POST':
        firstNameData = request.POST['first_name']
        emailData = request.POST['email']
        passwordData = request.POST['password']
        roleId = 2
        regionId = request.POST['region']
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


        regionData = region.objects.get(pk=regionId)
        

        if len(findLastUser) == 0:
            
            usernew = User.objects.create_user(username=usernameData,is_active=False,  password=passwordData,email=emailData,first_name=firstNameData,
            last_name='')
            usernew.save()

            dataToInsert = profile.objects.create(user=usernew,role=roleData,typeOfRegisteration=typeOfRegisterationData
            ,region=regionData,address=addressData
            ,phone=phoneData,mobile=phone2Data)
            dataToInsert.save()


            contextMail = {
                'nameReceiver':dataToInsert.user.first_name,
                'uid':urlsafe_base64_encode(force_bytes(usernew.pk)).decode(),
                'new_uuidOfProfile':str(account_activation_token.make_token(usernew))
                }
            subject = "Mhnaty Activation Link"
            html_content = render_to_string('mailTemplateActivateSendingNewCredentials.html', contextMail)
            email = EmailMessage(subject, html_content, to=[dataToInsert.user.email])
            try:
                email.content_subtype = 'html'
                email.send()
                Message = """An Email sent to your mailbox please check it
                برجاء مراجعة ايميلك لتفعيل الحساب
                """
                
            except Exception as e:
                Message = """Message not Sent Please Send the admin
                برجاء التواصل مع الادارة لوجود مشكلة ولم يتم ارسال ايميل التفعيل
                """
                print('-----------------------------------')
                print(e)

            user = authenticate(username=usernameData, password=passwordData)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/'+get_language()+'/')
            else:
                return HttpResponseRedirect('/'+get_language()+'/activation?Message='+Message)


    
    data = {
        'allCities':allCities
    }


    return render(request,'index_reg.html',data)



def activateNow(request,token):
    uidb64 = request.GET['uitoken']
    try:
        
        uid = force_text(urlsafe_base64_decode(bytes(uidb64,encoding='utf8')))

        user = User.objects.get(pk=uid)
    except Exception as ex:
        user = None
        print(ex)
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponseRedirect('/'+get_language()+'/')
    else:
        return HttpResponseRedirect('/'+get_language()+'/')

def activation(request):

    return render(request,'activation.html',None)

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



def getListOfcategoriesByparentOneId(request):
    
    with connection.cursor() as cursorLast:
    
        try:
            mainCategory = request.POST['mainCategory']
            
            if mainCategory !='':
                sql_query = """

                        select concat('{"Result":"Ok","Number":',count(*),',"data":[',group_concat(concat('{"id":',x.id,',"name":"',x.name,'"}')),']}')
                    as output 
                    from (
                    SELECT  category.id,category.name as name FROM category
                    where LOWER(category.parentCategory)=LOWER('"""+mainCategory+"""') ) x;



                    """
            else:
                sql_query = """

                            select concat('{"Result":"Ok","Number":',count(*),',"data":[',group_concat(concat('{"id":',x.id,',"name":"',x.name,'"}')),']}')
                    as output 
                    from (
                    SELECT  category.id,category.name as name FROM category
                    where category.isFirstHead=0
                    ) x;





                    """

            # print(sql_query)
            cursorLast.execute(sql_query)
            cursorAllData = cursorLast.fetchone()
        
            y=cursorAllData[0].replace('\r\n','')
            # print(y)
            return HttpResponse(y,content_type='application/json')
        except Exception as e:
            print(e)
            allJson = {"Result": "Fail"}
            return JsonResponse(allJson, safe=False)

       




def getListOfRegionsByCityId(request):
    
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
                    where LOWER(city.id)=LOWER('"""+city+"""') ) x;



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

       



def getListOfRegions(request):
    
    with connection.cursor() as cursorLast:
    
        try:
            city = request.POST['city']
            

            # print(city)
            if city !="''":
                sql_query = """

                        select concat('{"Result":"Ok","Number":',count(*),',"data":[',group_concat(concat('{"id":',x.id,',"name":"',x.name,'"}')),']}')
                    as output 
                    from (
                    SELECT  region.id,region.name as name FROM region
                    left join city on city.id = region.cityOfRegion_id
                    where LOWER(city.name) in ("""+city+""") ) x;



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

            # print(sql_query)
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

    citiesSearch = request.POST['citiesSearch']
    categoriesSearch = request.POST['categoriesSearch']
    experiensesSearch = request.POST['experiensesSearch']
    regionsSearch = request.POST['regionsSearch']
    rateMax = request.POST['rateMax']
    rateMin = request.POST['rateMin']
    typeOfOrder = request.POST['typeOfOrder']


    # print("KO:",citiesSearch)
    # print(rateMin)
    # print(city)
    # print(region)
    try:
        if citiesSearch!='' or categoriesSearch!='' or experiensesSearch!='' or regionsSearch!='' or rateMax!='' or rateMin!='':
            searchKey = 'Exists'


        print(searchKey)
        if searchKey == '':

            if category!='':
                categorySearch = Q(category__parentCategory=category)
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
            & Q(deleted=False)).order_by(typeOfOrder+'created')

        else:


            if categoriesSearch!='':
                categorySearch = Q(id__isnull=True) 
                for item in categoriesSearch.split(','):
                    categorySearch = categorySearch | Q(category__parentCategory=item)
            else:
                categorySearch = Q(id__isnull=False)


            if citiesSearch!='':
                citySearch = Q(id__isnull=True) 
                for item in citiesSearch.split(','):
                    citySearch = citySearch | Q(owner__region__cityOfRegion__name=item)
            else:
                citySearch = Q(id__isnull=False)


            
            if regionsSearch!='':
                regionSearch = Q(id__isnull=True) 
                for item in regionsSearch.split(','):
                    regionSearch = regionSearch | Q(owner__region__name=item)
            else:
                regionSearch = Q(id__isnull=False)


            if experiensesSearch!='':
                expSearch = Q(id__isnull=True) 
                for item in experiensesSearch.split(','):
                    expSearch = expSearch | Q(owner__tags__name__icontains = item)
            else:
                expSearch = Q(id__isnull=False)

            
            rateExpression = Avg(F('comments__rate'))
            if rateMax!='':
                rateMaxSearch = Q(rateFilter__lt = rateMax)
            else:
                rateMaxSearch = Q(id__isnull=False)


            if rateMin!='':
                rateMinSearch = Q(rateFilter__gt = rateMin)
            else:
                rateMinSearch = Q(id__isnull=False)


            # print(rateMaxSearch)
            allElements = theadd.objects.prefetch_related('comments').annotate(rateFilter = rateExpression).filter(Q(deleted=False) & 
            (categorySearch &
             citySearch     &
             regionSearch   &
             expSearch      &
             rateMaxSearch  &
             rateMinSearch)).order_by(typeOfOrder+'created')


        
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
    
    return render(request,'index_search.html',None)


@login_required
def profileWeb(request):
    user =request.user
    userobject = User.objects.filter(pk=user.id)
    userProfile = profile.objects.filter(user=user)
    userProfileMe = profile.objects.get(user__id=user.id)
    userLastProfile = user.profile_set.last()
    allCities = city.objects.filter(Q(deleted=False))
   
    getMyAdd = theadd.objects.filter(Q(deleted=False)& Q(owner__id=userProfileMe.id))
    

    try:
        theAddObj = theadd.objects.filter(Q(deleted=False)& Q(owner__id=userProfileMe.id)).last()
    except:
        theAddObj = None
        
    profilesOfTheAdd_ids = message.objects.filter(theadd=theAddObj).values_list('from_user',flat=True)
    profilesOfTheAdd = profile.objects.filter(id__in=profilesOfTheAdd_ids)


    allparentCategory = category.objects.filter(Q(deleted=False)&Q(isFirstHead=True))


    if len(getMyAdd)==0:
        categoryNow = category.objects.get(pk=1)
        getMyAdd = theadd.objects.create(name="",details="",category=categoryNow,owner=userProfileMe,mainImage=None,
        videoUrl="",featureAddNumber=0)
        try:
            parentCategory = category.objects.get(pk=getMyAdd.category.parentCategory)
        except:
            parentCategory = None
    else:
        getMyAdd = theadd.objects.filter(Q(owner__id=userProfileMe.id)&Q(deleted=False)).last()
        try:
            parentCategory = category.objects.get(pk=getMyAdd.category.parentCategory)
        except:
            parentCategory = None
    

    if request.method=='POST':
        typeOfForm = request.POST['typeOfForm']  

        if typeOfForm == 'mainData':

            nameData = request.POST['name'] 
            phoneData = request.POST['phone']
            addressData = request.POST['address']
            mobileData = request.POST['mobile'] 
            regionId = request.POST['region']

            regionData = region.objects.get(pk=regionId)
            userobject.update(first_name=nameData)
            userProfile.update(phone=phoneData,region=regionData,mobile=mobileData,address=addressData)
        elif typeOfForm == 'AddData':   
            # print(request.POST)
            userProfileMe.tags.all().delete()
            nameData = request.POST['name'] 
            
            aboutMeData = request.POST['aboutMe']
            detailsData = request.POST['details']
            categoryData = request.POST['category'] 
            videoData = request.POST['video']
            experienses = request.POST['experienses']

            allExperienses = experienses.split(",")
            for itemExp in allExperienses:
                if itemExp != '':
                    newTag = tag.objects.create(name=itemExp,propertyType=0)
                    newTag.save()
                    userProfileMe.tags.add(newTag)

            categoryData = category.objects.get(pk=categoryData)
            # userobject.update(first_name=nameData)
            userProfile.update(aboutMe=aboutMeData)
            getMyAdd = theadd.objects.filter(Q(owner__id=userProfileMe.id))
            getMyAdd.update(name=nameData,details=detailsData,category=categoryData,videoUrl=videoData)
            getMyAdd = theadd.objects.filter(Q(deleted=False)& Q(owner__id=userProfileMe.id)).last()

            try:
                parentCategory = category.objects.get(pk=getMyAdd.category.parentCategory)
            except:
                parentCategory = None


            attachments = request.POST.getlist('imagesAddFiles')
            for item_att in attachments:
                if item_att!='' and item_att!=None:
                    fileOld = attachmenttranscript.objects.filter(file = item_att).count()
                    if fileOld==0:
                        file_path = os.path.join(settings.MEDIA_ROOT, item_att)
                        file_type, file_encoding = mimetypes.guess_type(file_path)
                        fi = open(file_path, 'rb')
                        local_file = File(fi)
                        fileName = os.path.basename(local_file.name).split('``__``')[0]
                        
                        attachmetToAdd = attachmenttranscript.objects.create(file=local_file,content_type=file_type,name = fileName)
                        attachmetToAdd.save()
                        
                        local_file.close()
                        getMyAdd.images.add(attachmetToAdd)
                        default_storage.delete(item_att)

            allFiles = getMyAdd.images.all()
        elif typeOfForm == 'mainImage':
            userProfile = profile.objects.get(user=user)
            userProfile.image = request.FILES['file-input']
            
            userProfile.save()

        elif typeOfForm == 'addMainImage':
            getMyAdd = theadd.objects.filter(Q(deleted=False)& Q(owner__id=userProfileMe.id)).last()
            getMyAdd.mainImage = request.FILES['file-inputAddImage']
            
            getMyAdd.save()

    allFiles = getMyAdd.images.all()
    allTags = getMyAdd.owner.tags.all()
    allTagsArray = list(allTags)
    allTagsDelemited = ','.join(map(str, allTagsArray))
    print(allTagsDelemited)


    data = {
        'allparentCategory':allparentCategory,
        'allCities':allCities,
        'getMyAdd':getMyAdd,
        'allFiles':allFiles,
        'allTags':allTags,
        'allTagsDelemited':allTagsDelemited,
        'parentCategory':parentCategory,
        'theAddObj': theAddObj,
        'profilesOfTheAdd':profilesOfTheAdd,
    }
        
    return render(request,'profile.html',data)




@login_required
def controlpanel(request):
    user =request.user
    userobject = User.objects.filter(pk=user.id)
    userProfile = profile.objects.filter(user=user)
    userProfileMe = profile.objects.get(user__id=user.id)
    userLastProfile = user.profile_set.last()
   
    
    try:
        theAddObj = theadd.objects.get( id=settings.ID_ADD_ADMIN)
    except:
        theAddObj = None
        
    profilesOfTheAdd_ids = message.objects.filter(theadd=theAddObj).values_list('from_user',flat=True)
    profilesOfTheAdd = profile.objects.filter(id__in=profilesOfTheAdd_ids).exclude(id=userProfileMe.id)

    data = {
        'theAddObj': theAddObj,
        'profilesOfTheAdd':profilesOfTheAdd,
    }
        

    return render(request,'controlpanel.html',data)





@login_required
def uploadFiles_ForAdd(request):
    if request.method=='POST':
        if request.FILES:
            for f in request.FILES.getlist('imagesAddFiles'):
                upload_to = 'docs/temp/'
                ext = f.name.split('.')[-1]
                filename = '{}.{}'.format(f.name.split('.')[0]+'.'+ext+'``__``'+uuid4().hex, ext)
                default_storage.save(os.path.join(upload_to, filename), f)
        response = HttpResponse(os.path.join(upload_to, filename))

    elif request.method=='DELETE':
        data_bytes = request.body
        data_string = data_bytes.decode('utf-8')
        try:
            attachmenttranscript.objects.filter(file = data_string).delete()
        except:
            pass
        response = HttpResponse(str(data_string))
    
    elif request.method=='GET':
        file = request.GET['load']
        fileNew = attachmenttranscript.objects.filter(file=file)[0]
        response = HttpResponse(fileNew.file)
        response['Content-Disposition'] = 'attachment; filename="'+str(fileNew.name)+'"'
        response['Content-Type'] = fileNew.content_type
        response['Access-Control-Expose-Headers'] = 'Content-Disposition, Content-Length, X-Content-Transfer-Id'
        response['X-Content-Transfer-Id'] = str(fileNew.file.name)
        
        
    return response




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


    data = {
    }
    return render(request,'index.html',data)

def getAllCategoriesJson(request):
    with connection.cursor() as cursorLast:

        try:
            category = request.POST['category']
            
            if category !='':
                sql_query = """

                        select concat('{"Result":"Ok","Number":',count(*),',"data":[',group_concat(concat('{"id":',x.id,',"name":"',x.name,'"}')),']}')
                    as output 
                    from (
                    SELECT  category.id,category.name as name FROM category
                    where  isFirstHead=1 and deleted=0 and LOWER(category.name) like LOWER('%"""+category+"""%') ) x;



                    """
            else:
                sql_query = """

                            select concat('{"Result":"Ok","Number":',count(*),',"data":[',group_concat(concat('{"id":',x.id,',"name":"',x.name,'"}')),']}')
                    as output 
                    from (
                    SELECT  category.id,category.name as name FROM category
                    where isFirstHead=1 and deleted=0
                    ) x;





                    """
            
            # print(sql_query)

            cursorLast.execute(sql_query)
            cursorAllData = cursorLast.fetchone()
            y=cursorAllData[0].replace('\r\n','')
            # print(y)
            return HttpResponse(y,content_type='application/json')
        except Exception as e:
            print(e)
            allJson = {"Result": "Fail"}
            return JsonResponse(allJson, safe=False)



def getAllAdsByCategoriesJson(request):
    with connection.cursor() as cursorLast:

        try:
            category = request.POST['category']
            
            if category !='':
                sql_query = """




                        select concat('{"Result":"Ok","Number":',count(*),',"data":[',group_concat(concat('{"id":',x.id,',"name":"',x.nametheadd,' (',namecategory,')"}')),']}')
                    as output
                    from (
                    select theadd.id,theadd.name as nametheadd,category.name as namecategory FROM theadd
                    LEFT join  category on category.id=theadd.category_id
                    where  theadd.deleted=0 and LOWER(category.name) like LOWER('%"""+category+"""%') ) x;





                    """
            else:
                sql_query = """

                     
                        select concat('{"Result":"Ok","Number":',count(*),',"data":[',group_concat(concat('{"id":',x.id,',"name":"',x.nametheadd,' (',namecategory,')"}')),']}')
                    as output
                    from (
                    select theadd.id,theadd.name as nametheadd,category.name as namecategory FROM theadd
                    LEFT join  category on category.id=theadd.category_id
                    where  theadd.deleted=0 and LOWER(category.name) like LOWER('%ط%') ) x;






                    """
            
            print(sql_query)

            cursorLast.execute(sql_query)
            cursorAllData = cursorLast.fetchone()
            y=cursorAllData[0].replace('\r\n','')
            # print(y)
            return HttpResponse(y,content_type='application/json')
        except Exception as e:
            print(e)
            allJson = {"Result": "Fail"}
            return JsonResponse(allJson, safe=False)






def getAllTagsJson(request):
    SearchQuery =request.GET['query'] 

    try:
        sql_query = """

                select concat('[',group_concat(concat('{"value":"',x.name,'","text":"',x.name,'","continent":"',x.name,'"}')),']')
                        as output 
                        from (
                        SELECT  tag.id,tag.name as name FROM tag
                        where tag.deleted=0 and tag.name like '%"""+SearchQuery+"""%'
                        group by tag.name 
                        ) x;


                """

        # print(sql_query)
        with connection.cursor() as cursorLast:
            cursorLast.execute(sql_query)
            cursorAllData = cursorLast.fetchone()
            y=cursorAllData[0].replace('\r\n','')
            # print(y)
        return HttpResponse(y,content_type='application/json')
    except Exception as e:
            print(e)
            allJson = {"Result": "Fail"}
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



def mainBeforeLanguage(request):

    
    return HttpResponseRedirect('/ar')

def getAllExperiansesJson(request):
    with connection.cursor() as cursorLast:

        try:
            tag = request.POST['tag']
            
            if tag !='':
                sql_query = """

                        select concat('{"Result":"Ok","Number":',count(*),',"data":[',group_concat(concat('{"id":',x.id,',"name":"',x.name,'"}')),']}')
                    as output 
                    from (
                    SELECT  tag.id,tag.name as name FROM tag
                    where deleted=0 and LOWER(tag.name) like LOWER('%"""+tag+"""%') 
                    group by tag.name) x;



                    """
            else:
                sql_query = """

                            select concat('{"Result":"Ok","Number":',count(*),',"data":[',group_concat(concat('{"id":',x.id,',"name":"',x.name,'"}')),']}')
                    as output 
                    from (
                    SELECT  tag.id,tag.name as name FROM tag
                    where  deleted=0
                    group by tag.name
                    ) x;





                    """
            
            # print(sql_query)

            cursorLast.execute(sql_query)
            cursorAllData = cursorLast.fetchone()
            y=cursorAllData[0].replace('\r\n','')
            # print(y)
            return HttpResponse(y,content_type='application/json')
        except Exception as e:
            print(e)
            allJson = {"Result": "Fail"}
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




@login_required
def showUserMessages(request, id):
    theaddObj  = get_object_or_404(theadd,id=id) 
    # print(theaddObj.owner.id)
    user =request.user
    userProfile = profile.objects.filter(user=user).last()
    if userProfile.id == theaddObj.owner.id:
        allowSend = False
    else:
        allowSend = True
    # print(user.first_name)
    if request.method == 'POST':
        message_text = request.POST.get('input_message')

        messageobj = message.objects.create( from_user = user.profile_set.last(), to_user = theaddObj.owner, theadd = theaddObj, message= message_text)
   
    messages = message.objects.filter(
        Q(deleted=False) &  
        (Q(from_user = user.profile_set.last().id ) | Q(from_user = theaddObj.owner.id)) & 
        (Q(to_user =  theaddObj.owner.id) | Q(to_user =  user.profile_set.last().id)) &
        (Q(theadd = theaddObj))
        ).order_by('created')

    context = {
        'messages' : messages,
        'theaddObj':theaddObj,
        'imageOFImageOwner':theaddObj.owner.image.url if theaddObj.owner.image!=None else '/static/Img/blank-profile-picture-973460_640.png' ,
        'imageOFImageMe':user.profile_set.last().image.url if user.profile_set.last().image!=None else '/static/Img/blank-profile-picture-973460_640.png' ,
        'allowSend':allowSend
    }
    return render(request, 'showUserMessages.html', context)



@login_required
def getProfileMessages(request):
    idOfFromUserProfile = request.POST['idOfFromUserProfile']
    userProfile = get_object_or_404(profile,id=idOfFromUserProfile)

    idOfProfileOfTheAdd = request.POST['idOfProfileOfTheAdd']
    theaddObj  = get_object_or_404(theadd,id=idOfProfileOfTheAdd) 

    messages = message.objects.filter(
        Q(deleted=False) &  
        (Q(from_user = userProfile.id ) | Q(from_user = theaddObj.owner.id)) & 
        (Q(to_user =  theaddObj.owner.id) | Q(to_user =  userProfile.id)) &
        (Q(theadd = theaddObj))
        ).order_by('created')
   
    messagesData = []
    for item in list(messages):
        messagesData.append(item.to_json())

    response={
      'imageOfCurrentChat':userProfile.image.url if userProfile.image!=None else '/static/Img/blank-profile-picture-973460_640.png' ,
      'nameOfCurrentChat':userProfile.user.first_name,
      'numberOfCurrentChat':str(len(messages)),
      'messagesData':messagesData, 

    }

    # print(response)
    return JsonResponse(response, safe=False)

   
@login_required
def sendMessage(request):
    messageContent = request.POST['messageContent']
    theaddId       = request.POST['theaddId']
    fromProfileId  = request.POST['fromProfileId']
    idOfToUserProfile = request.POST['idOfToUserProfile']


    toUserProfile = profile.objects.get(id=idOfToUserProfile)
    theaddObj      = theadd.objects.get(id = theaddId)
    fromProfileObj = profile.objects.get(id = fromProfileId )

    user = request.user
    profileobj=user.profile_set.last()

    messageObj = message.objects.create(message = messageContent, to_user = toUserProfile, theadd = theaddObj, from_user = theaddObj.owner)
    
    message_queryset = message.objects.filter(id=messageObj.id)
    messagesData = []
    for item in list(message_queryset):
        messagesData.append(item.to_json())

    response={
      'messagesData':messagesData,  

    }

    # print(response)
    return JsonResponse(response, safe=False)





   
@login_required
def sendMessageToTheAdd(request):
    messageContent = request.POST['messageContent']
    theaddId       = request.POST['theaddId']
    fromProfileId  = request.POST['fromProfileId']
    idOfToUserProfile = request.POST['idOfToUserProfile']


    toUserProfile = profile.objects.get(id=idOfToUserProfile)
    theaddObj      = theadd.objects.get(id = theaddId)
    fromProfileObj = profile.objects.get(id = fromProfileId )

    user = request.user
    profileobj=user.profile_set.last()

    messageObj = message.objects.create(message = messageContent, from_user = toUserProfile, theadd = theaddObj, to_user = theaddObj.owner)
    
    message_queryset = message.objects.filter(id=messageObj.id)
    messagesData = []
    for item in list(message_queryset):
        messagesData.append(item.to_json())

    response={
      'messagesData':messagesData,  

    }

    # print(response)
    return JsonResponse(response, safe=False)




    