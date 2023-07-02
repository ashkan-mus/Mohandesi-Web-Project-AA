from multiprocessing import Value
import queue
from urllib import request
from django.shortcuts import render , redirect
from django.db.models import Count
from django.http import HttpResponse , JsonResponse
from django.views import View

from config import settings
from . models import Customer, OrderPlaced, Product , Card
from . forms import CustomerProfileForm, CustomerRegistrationForm
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,"store/home.html")
def about(request):
    return render(request,"store/about.html")
def contact(request):
    return render(request,"store/contact.html")

class CategoryView(View):
    def get(self, request,val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request,"store/category.html",locals())

class CategoryTitle(View):
    def get(self, request,val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request,"store/category.html",locals())

class ProductDetail(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request, "store/productdetail.html",locals())


class CustomerRegistrationView(View):

    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request, "store/customerregistration.html",locals())
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"You Register Successfully")
        else:
            messages.error(request,"Invalid Input Data")
        return render(request, "store/customerregistration.html",locals())
    
class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request, "store/profile.html",locals())
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            reg = Customer(user=user,name= name , locality= locality , city = city)
            reg.save()
            messages.success(request,"Profile Saved")
        else:
            messages.error(request,"Invalid Input Data")
        return render(request, "store/profile.html",locals())
    
def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, "store/address.html")


class updateAddress(View):
    def get(self,request,pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        return render(request, "store/updateAddress.html",locals())
    def post(self,request,pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.locality = form.cleaned_data['locality ']
            add.city = form.cleaned_data['city']
           
            add.save()
            messages.success(request,"Profile Saved")
        else:
            messages.error(request,"Invalid Input Data")



        return render(request, "store/updateAddress.html",locals())
    
def add_to_card(request):
     user=request.user
     product_id=request.GET.get('prod_id')
     product = Product.objects.get(id=product_id)
     Card(user=user,product=product).save()
     return redirect("/card")
def show_card(request):
    user = request.user
    card = Card.objects.filter(user=user)

    return render(request, "store/addtocard.html", locals())

class checkout(View):
    def get(self,request):
        user = request.user
        card = Customer.objects.filter(user=user)
        card_items = Card.objects.filter(user=user)
        famount = 0
        for p in card_items:
            value = p.quantity * p.product.selling_price
            famount = famount + value
            totalamount = famount + 40
            razoramount = int(totalamount * 100)
            client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
            data = { "amount":razoramount , "currency" :"TMN" , "receipt" : "order_rcptid_12" } 
            payment_reponse = client.order.create(data=data)
            print(payment_response)

        return render(request, "store/checkout.html", locals())


def orders(request):
    order_placed = OrderPlaced.objects.filter(user=request.user)
    return render(request, "store/orders.html", locals())


def plus_card(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c = Card.objects.get( queue (product=prod_id) & queue (user=request.user))
        c.quantity+=1
        c.save()
        user = request.user
        card = Card.objects.filter(user=user)
        amount = amount + Value
        totalamount = amount + 40
        data={
            'quantity' : c.quantity,
            'amount':amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)
    
def minus_card(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c = Card.objects.get( queue (product=prod_id) & queue (user=request.user))
        c.quantity+=1
        c.save()
        user = request.user
        card = Card.objects.filter(user=user)
        amount = amount + Value
        totalamount = amount + 40
        data={
            'quantity' : c.quantity,
            'amount':amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)
    
def remove_card(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c = Card.objects.get( queue (product=prod_id) & queue (user=request.user))
        c.quantity+=1
        c.delete()
        user = request.user
        card = Card.objects.filter(user=user)
        amount = amount + Value
        totalamount = amount + 40
        data={
            'quantity' : c.quantity,
            'amount':amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)