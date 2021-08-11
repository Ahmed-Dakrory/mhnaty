from django.http import JsonResponse
from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.conf import settings  # this is a good example of extra
                                  # context you might need across templates


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.db.models import Q
from django.utils import translation
from django.views.generic.base import View
from .models import *


def defaultContextProcessor(request):
    # you can declare any variable that you would like and pass 
    # them as a dictionary to be added to each template's context:
    user =request.user
    if user.is_authenticated:
        userProfile = profile.objects.get(user=user)
    else:
        userProfile = None

    return dict(
        userProfile = userProfile,
        current_date = datetime.now()    
    )
