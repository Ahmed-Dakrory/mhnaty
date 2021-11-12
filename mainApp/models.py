from django.db import models
from django.contrib.auth.models import User
from django.core.validators import int_list_validator
from uuid import uuid4
import os
from django.db.models import Avg
# Create your models here.



def path_and_renameListing(instance, filename):
    upload_to = 'files_to_upload/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)



class city(models.Model):
    name = models.CharField(max_length=500,default=None)
    created = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)


    class Meta:
        db_table = "city"


    def to_json(self):
        return {
            'id' :self.id,
            'name':self.name
            }
        

    def __str__(self):
        return self.name




class region(models.Model):
    cityOfRegion = models.ForeignKey(city, on_delete=models.PROTECT)
    name = models.CharField(max_length=500,default=None)
    created = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)


    class Meta:
        db_table = "region"


    def to_json(self):
        return {
            'id' :self.id,
            'name':self.name
            }
        

    def __str__(self):
        return self.name

class permissiongeneral(models.Model):
    name = models.CharField(max_length=500,default=None)
    created = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)


    class Meta:
        db_table = "permissiongeneral"


    def to_json(self):
        return {
            'id' :self.id,
            'name':self.name
            }
        

    def __str__(self):
        return self.name


class role(models.Model):
    permissiongeneral = models.ManyToManyField(permissiongeneral)
    name = models.CharField(max_length=500,default=None)
    created = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    

    class Meta:
        db_table = "role"


    def to_json(self):
        return {
            'id' :self.id,
            'name': self.name,
            'created': self.created,
            'numberOfPermissions': len(self.permissiongeneral.all())
            }
        

    def __str__(self):
        return self.id




class tag(models.Model):
    name = models.CharField(max_length=500,default=None,null=True)
    propertyType = models.IntegerField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)


    class Meta:
        db_table = "tag"


    def to_json(self):
        return {
            'id' :self.id,
            'name':self.name,
            'propertyType':self.propertyType
            }
        

    def __str__(self):
        return self.name


class profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    aboutMe = models.TextField(default=None,null=True)
    address = models.CharField(max_length=500,default=None,null=True)
    phone = models.CharField(max_length=500,default=None,null=True)
    region =  models.ForeignKey(region, on_delete=models.PROTECT,null=True)
    mobile = models.CharField(max_length=500,default=None,null=True)

    
    tags = models.ManyToManyField(tag)
    # normal 0
    #facebook 1
    #gmail  2
    typeOfRegisteration = models.CharField(max_length=500,default='Normal', null=True)
    image = models.ImageField(upload_to='attachments/userData/',null=True)
    role = models.ForeignKey(role, on_delete=models.PROTECT,null=True)
    created = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)


    class Meta:
        db_table = "profile"


    def to_json(self):
        return {
            'id' :self.id,
            'username':self.user.username,
            'email':self.user.email,
            'role':self.role.name,
            'job':self.job.name
            }
        

    def __str__(self):
        return self.user.username


class attachmenttranscript(models.Model):
    file = models.FileField('ListDoc', upload_to=path_and_renameListing)
    postDate = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    content_type = models.CharField(max_length=500,default=None)
    name = models.CharField(max_length=5000,default=None)
    
    
    @property
    def filename(self):
        name = self.file.name.split("/")[1].replace('_',' ').replace('-',' ')
        return name

    
    class Meta:
        db_table = "attachmenttranscript"


class category(models.Model):
    name = models.CharField(max_length=500,default=None)
    isFirstHead = models.BooleanField(default=False)
    details = models.CharField(max_length=500,default=None,null=True)
    image = models.ImageField(upload_to='attachments/allImages/',null=True)
    parentCategory = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)


    class Meta:
        db_table = "category"


    def to_json(self):
        return {
            'id' :self.id,
            'name':self.user.username,
            'image':self.image
            }
        

    def __str__(self):
        return self.name



class reply(models.Model):
    fromUser = models.ForeignKey(profile, on_delete=models.PROTECT,related_name='fromUser')
    details = models.TextField(default=None)
    created = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)


    class Meta:
        db_table = "reply"


    def to_json(self):
        return {
            'id' :self.id,
            'details':self.details,
            'username':self.fromUser.user.first_name,
            
            'image':self.fromUser.image.url if self.fromUser.image!=None else '/static/images/blank-profile-picture-973460_640.png' ,
            'created':self.created,
            }
    


class comment(models.Model):
    fromUser = models.ForeignKey(profile, on_delete=models.PROTECT,related_name='fromUserMainComment')
    details = models.TextField(default=None)
    replies = models.ManyToManyField(reply)
    rate = models.FloatField(blank=True, null=True)


    created = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)


    class Meta:
        db_table = "comment"


    def to_json(self):
        return {
            'id' :self.id,
            'details':self.details,
            'username':self.fromUser.user.first_name,
            'rate':self.rate,
            'image':self.fromUser.image.url,
            'replies': [replyItem.to_json() for replyItem in self.replies.all()],
            'created':self.created,
            }
    

class theadd(models.Model):
    owner = models.ForeignKey(profile, on_delete=models.PROTECT)
    name = models.CharField(max_length=500,default=None)
    details = models.TextField(default=None)
    price = models.FloatField(blank=True, null=True)
    categoryMain = models.ForeignKey(category, on_delete=models.PROTECT)
    images = models.ManyToManyField(attachmenttranscript)
    videoUrl = models.TextField(default=None,null=True)
    mainImage = models.ImageField(upload_to='attachments/mainImage/',null=True)
    
    featureAddNumber = models.IntegerField(default=0,null=True)

    subcategories = models.ManyToManyField(category, blank=True,related_name="subcategories")
    comments = models.ManyToManyField(comment)
    created = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)


    class Meta:
        db_table = "theadd"
        ordering = ['-created']

    def avg_ratings(self):
        # return 3.5
        if self.comments.aggregate(Avg('rate'))['rate__avg'] != None:
            return self.comments.aggregate(Avg('rate'))['rate__avg']
        else:
            return 0


    def to_json(self):
        return {
            'id' :self.id,
            'name':self.name,
            'featureAddNumber':self.featureAddNumber,
            'owner':self.owner.user.first_name,
            'phone':self.owner.phone,
            'averageRate':0 if self.comments.aggregate(Avg('rate'))['rate__avg'] == None else self.comments.aggregate(Avg('rate'))['rate__avg'] ,
            'address':self.owner.address,
            'details':self.details,
            'mainImage':self.mainImage.url,
            'category_name':self.categoryMain.name,
            }
        

    def __str__(self):
        return self.name





class message(models.Model):
    from_user = models.ForeignKey(profile, on_delete=models.PROTECT,related_name='messageFromUser')
    to_user   = models.ForeignKey(profile, on_delete=models.PROTECT,related_name='messageToUser')
    theadd    = models.ForeignKey(theadd, on_delete=models.PROTECT,related_name='messageTheadd')

    message   = models.TextField(max_length=500,default=None,null=True)

    created = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)


    class Meta:
        db_table = "messages"


    # def to_json(self):
    #     return {
    #         'id' :self.id,
    #         'from_user':self.from_user.user.name,
    #         'to_user':self.to_user.owner.user.name,
    #         'messages':self.messages,
    #         'sendDate':self.created
    #         }

    def to_json(self):
        return {
            'id' :self.id,
            'from_user__id':self.from_user.id,
            'from_user__user__username':self.from_user.user.first_name,
            'theadd__owner__user__username':self.theadd.owner.user.first_name,
            'message':self.message,
            'created':self.created,
            'from_user_image':self.from_user.image.url if self.from_user.image!=None and self.from_user.image!='' else '/static/images/blank-profile-picture-973460_640.png' ,
            }
        