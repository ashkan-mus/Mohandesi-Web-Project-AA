from django.contrib import admin
from . models import Product , Customer , Card , Payment ,OrderPlaced
# Register your models here.
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','weight','category','product_image']

@admin.register(Customer)
class CustomertModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','locality','city']


@admin.register(Card)
class CardModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']

@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','amount','razorpay_order_id', 'razorpay_payment_id', 'paid']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id','customer','product','quantity' , 'ordered_date' , 'payment']