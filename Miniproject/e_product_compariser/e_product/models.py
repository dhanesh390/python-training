from django.db import models
from .myconstants import constants
from datetime import datetime


# Create your models here.
class User(models.Model):
    """ This class contains the attributes of user object"""
    user_id = models.CharField(max_length=10)
    user_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=10)
    email_id = models.EmailField(max_length=100)
    password = models.CharField(max_length=20)
    is_active_user = True
    created_on = datetime.utcnow().strftime(constants.DATE_TIME_FORMAT)
    updated_on = datetime.utcnow().strftime(constants.DATE_TIME_FORMAT)


class ShopDetails(models.Model):
    """ This class contains the attributes of shop details object"""
    shop_id = models.UUIDField(max_length=6)
    shop_name = models.CharField(max_length=100)
    building_no = models.CharField(max_length=30)
    street_name = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    pincode = models.BigIntegerField
    created_on = datetime.utcnow().strftime(constants.DATE_TIME_FORMAT)
    updated_on = datetime.utcnow().strftime(constants.DATE_TIME_FORMAT)


class Category(models.Model):

    category_id = models.UUIDField
    category_type = models.CharField(max_length=100)
    specifications = models.CharField(max_length=1000)
    created_on = datetime.utcnow().strftime(constants.DATE_TIME_FORMAT)
    updated_on = datetime.utcnow().strftime(constants.DATE_TIME_FORMAT)


class Product(models.Model):

    product_id = models.AutoField
    product_name = models.CharField(max_length=100)
    product_price = models.BigIntegerField
    product_quantity = models.FloatField
    product_category = models.CharField(max_length=100)
    product_availability = models.BooleanField
    created_on = datetime.utcnow().strftime(constants.DATE_TIME_FORMAT)
    updated_on = datetime.utcnow().strftime(constants.DATE_TIME_FORMAT)


