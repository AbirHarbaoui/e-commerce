from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from django.db.models import Count
from django.contrib import messages
from .models import Customer
from .models import Product
from .forms import CustomerRegistrationForm
from .forms import CustomerProfileForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView



def home(request):
    return render(request,"app/home.html")


def about(request):
    return render(request,"app/about.html")


def contact(request):
    return render(request,"app/contact.html")

class CategoryView(View):
    def get(self,request,val):
        product = Product.objects.filter(category=val)
        title = product.values('title').annotate(total=Count('title'))
        return render(request,"app/category.html",locals())

class CategoryTitle(View):
    def get(self,request,val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request,"app/category.html",locals())


class ProductDetail(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request,"app/productdetail.html",locals())




class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request,"app/customerregistration.html",locals())
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"congratulations !User Register Successfulyy")
        else :
            messages.warning(request,"Invalid Input Data")
        return render(request,'app/customerregistration.html', locals())
    

class CustomLoginView(LoginView):
    success_url = '/profile/'  # Remplacez '/profile/' par l'URL de votre page de profil


class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request,"app/profile.html",locals())
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']

            reg=Customer(user=user,name=name,locality=locality,mobile=mobile,city=city,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request,"congratulations ! Profile Save Successfuly")
        else :
            messages.warning(request,"Invalid Input Data")   
        return render(request,"app/profile.html",locals())


def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request,'app/address.html',locals())


class updateAddress(View):
    def get(self,request,pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        return render(request,"app/updateAddress.html",locals())
    def post(self,request,pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            add.mobile = form.cleaned_data['mobile']
            add.state = form.cleaned_data['state']
            add.zipcode = form.cleaned_data['zipcode']
            add.save()
            messages.success(request,"congratulations ! Profile Save Successfuly")
        else :
            messages.warning(request,"Invalid Input Data")   
        return redirect("address")
        