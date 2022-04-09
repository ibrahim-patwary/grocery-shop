from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Items, Subscribe,contact


# Create your views here.
def home(request):
    if request.method == 'POST':
            home = Subscribe()
            email = request.POST.get('sub_email')
            home.people=email
            home.save()
    context = {
        

    }
    return render(request, "1_home.html", context)
    
def Shop(request):
    allSHopItems = Items.objects.all()
    context={
        "allSHopItems":allSHopItems
    }
    return render(request, "2_shop.html", context)
def About(request):
    return render(request, "3_about.html")
def Review(request):
    return render(request, "4_review.html")
def Blog(request):
    return render(request, "5_blog.html")
def Contact(request):
        if request.method == 'POST':
            Contact = contact()
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            Contact.name=name
            Contact.email=email
            Contact.subject=subject
            Contact.phone=phone
            Contact.message=message
            Contact.save()
        return render(request, "6_contact.html")



def Sing_up(request):

    return render(request, "9_sing_in_up_container.html")



def handle_singUp(request):
    if request.method == "POST":
        userName = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        if pass1 != pass2:
            return redirect("/") 
        else:  
            

            try:
                myUser = User.objects.create_user(userName,email,pass1)
                myUser.save()
                messages.success(request,"Your account has been created!")
                return redirect("/") 
            except:
                messages.error(request,"The username already exist!")
                return redirect("/")
                    
    else:
        return HttpResponse("404-Not found the page")


def handle_login(request):
    if request.method == "POST":
        loginUserName = request.POST['loginUserName']
        Loginpass = request.POST['Loginpass']

        user = authenticate(username = loginUserName,password = Loginpass)
        if user is not None:
            login(request,user)
            messages.success(request,f"welcome {user.first_name}. You can order any Kind of websie you required!")
            return redirect("/")
        else:
            messages.error(request,"You don't have any account,Please create an account!")
            return redirect("/")

    return redirect("/")


#logout account
def handle_logout(request):
    logout(request)
    messages.success(request,"You successfully logout!")
    return redirect("/")

def show_data(request) :
        data=contact.objects.all()
        return render(request,'show_data.html',{"contact":data})
