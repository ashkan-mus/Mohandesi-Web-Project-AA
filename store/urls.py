from django.urls import path 
from . import views 
from django.conf import settings 
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm , MyPasswordResetForm

urlpatterns = [
    path("", views.home),
    path("about/", views.about, name = "about"),
    path("contact/", views.contact , name ="contact"),
    path("category/<slug:val>", views.CategoryView.as_view(), name="category"),
    path("product-detail/<int:pk>", views.ProductDetail.as_view(), name="product-detail"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("address/", views.address, name="address"),
    path("updateAddress/<int:pk>", views.updateAddress.as_view(), name="updateAddress"),

    path("add-to-card/>", views.add_to_card, name="add-to-card"),
    path("card/>", views.show_card, name="showcard"),
    path("checkout/>", views.checkout.as_view(), name="checkout"),

    path("pluscard/>", views.plus_card, name="pluscard"),
    path("minuscard/>", views.minus_card, name="minuscard"),
    path("removecard/>", views.remove_card, name="removecard"),
    path("orders/>", views.orders, name="orders"),


    
    #login auth

    path("registration/", views.CustomerRegistrationView.as_view(), name="customerregistration"),



    path("accounts/login", auth_view.LoginView.as_view(template_name='store/login.html', authentication_form=LoginForm), name="login"),


    path("password-reset", auth_view.PasswordResetView.as_view(template_name='store/password_reset.html', form_class=MyPasswordResetForm), name="password_reset"),
    
    path("logout/", auth_view.LogoutView.as_view
    (next_page='login'), name="logout"),
    
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)