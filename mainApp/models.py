from django.db import models
from django.contrib.auth.models import User
from django.core.validators import int_list_validator
from uuid import uuid4
import os
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


class permissionGeneral(models.Model):
    name = models.CharField(max_length=500,default=None)
    created = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)


    class Meta:
        db_table = "permissionGeneral"


    def to_json(self):
        return {
            'id' :self.id,
            'name':self.name
            }
        

    def __str__(self):
        return self.name


class role(models.Model):
    permissionGeneral = models.ManyToManyField(permissionGeneral)
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
            'numberOfPermissions': len(self.permissionGeneral.all())
            }
        

    def __str__(self):
        return self.id

class profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    address = models.CharField(max_length=500,default=None)
    phone = models.CharField(max_length=500,default=None)
    mobile = models.CharField(max_length=500,default=None,null=True)
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