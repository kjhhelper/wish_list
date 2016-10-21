from __future__ import unicode_literals
from django.db import models
import re, bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[a-zA-Z]*$')


class LogMgr(models.Manager):
    def validate(self,name,email,pwd,confirmpwd):
        errors=[]
        if len(name) < 2:
            errors.append("name is required")
        elif not NAME_REGEX.match(name):
            errors.append("Invalid first name")
        if len(email) < 2:
            errors.append("Email is required")
        elif not EMAIL_REGEX.match(email):
            errors.append("Invalid email")
        if len(pwd) is 0:
            errors.append("Password is required")
        elif len(pwd)<8:
            errors.append("Password must be at least 8 characters")
        elif not pwd == confirmpwd:
            errors.append("Password must match the Password Confirmation")
        if len(errors) is not 0:
            print('****validate****false********')
            return (False, errors)
        password = pwd.encode()
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        # print ('validate done')
        f=Log.logMgr.create(name=name, email=email, pwd=hashed)
        f.save()
        # print ('validate done done')
        return (True, f)

    def vali(self,item):
        errors=[]
        if len(item) < 4:
            errors.append("item is required")

        if len(errors) is not 0:
            # print('****validate****false********')
            return (False, errors)
        # print ('validate done')
        i=Log.logMgr.create(item=item)
        i.save()
        # print ('validate done done')
        return (True, i)

    def login(self, email, pwd):
        errors = []
        try:
            x = User.logMgr.get(email = email)
        except:
            errors.append("Email is required")
            return (False, errors)
        if len(pwd) is 0:
            errors.append("Password is required")
        elif not bcrypt.hashpw(pwd.encode(), x.pwd.encode()) ==  x.pwd.encode():
            errors.append("Incorrect password")
        if len(errors) is not 0:
            return (False, errors)
        x.save()
        return (True, x)


class Log(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    pwd = models.CharField(max_length=100)
    item = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    logMgr = LogMgr()
