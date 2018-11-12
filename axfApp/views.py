from django.shortcuts import render,redirect
from django.http import HttpResponse
from axfApp.models import Product,Category,Child

# Create your views here.
def index(request):
    return render(request,"common/base.html")

def home(request):
    return render(request,"home/home.html")

def market(request):
    # 获取组信息
    categories = Category.objects.all()

    # 获取显示商品信息
    products = Product.objects.filter(category_id="103606")


    return render(request,"market/market.html",{"categories":categories,"products":products})






def cart(request):
    return render(request,"cart/cart.html")

def mine(request):
    return render(request,"mine/mine.html")