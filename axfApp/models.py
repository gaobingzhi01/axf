from django.db import models

# Create your models here.

class AxfManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(isDelete=False)

# 商品表
class Product(models.Model):
    objects = AxfManager()
    name = models.CharField(max_length=20)
    longName = models.CharField(max_length=40)
    productId = models.CharField(max_length=20)
    storeNums = models.IntegerField()
    specifics = models.CharField(max_length=20)
    sort = models.IntegerField()
    marketPrice = models.FloatField()
    price = models.FloatField()
    category = models.ForeignKey("Category")
    child = models.ForeignKey("Child")
    img = models.CharField(max_length=200)
    keywords = models.CharField(max_length=40)
    brandId = models.CharField(max_length=20)
    brandName = models.CharField(max_length=40)
    safeDay = models.CharField(max_length=20)
    safeUnit = models.CharField(max_length=20)
    safeUnitDesc = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    class Meta:
        db_table = "products"

#分组表
class Category(models.Model):
    objects = AxfManager()
    id = models.CharField(max_length=20,primary_key=True)
    name = models.CharField(max_length=20)
    sort = models.IntegerField()
    isDelete = models.BooleanField(default=False)
    class Meta:
        db_table = "categories"

# 子组表
class Child(models.Model):
    objects = AxfManager()
    id = models.CharField(max_length=20,primary_key=True)
    name = models.CharField(max_length=20)
    sort = models.IntegerField()
    category = models.ForeignKey("Category")
    isDelete = models.BooleanField(default=False)
    class Meta:
        db_table = "children"
