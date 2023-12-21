from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Account,SimpleUser,Portfolio,Admin
from .forms import newPortflioForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import auth
from django.contrib import messages
# Create your views here.
def home(Request):
    accounts=Account.objects.all();
    # accounts_logins=[];
    # for acccount in accounts:
    #     accounts_logins.append(acccount.login)
    # responseHtml='<br>'.join(accounts_logins)
    # return HttpResponse(responseHtml)
    return render(Request,'accounts.html',{'accounts':accounts})
def homeUser(Request):
    accounts=Account.objects.all();
    return render(Request,'accountsForSimpleUser.html',{'accounts':accounts})
def acceuil(Request):
    users=SimpleUser.objects.all()
    # portfolios_count = Portfolio.objects.count()
    return render(Request,'home.html',{'users':users})

def showAllPortfolios(Request):
    portfolios=Portfolio.objects.all()
    #account=Account.objects.get(pk=accountId)
    return render(Request,'portfolios.html',{'portfolios':portfolios})

def showOneAccount(Request,accountId):
    
    account=Account.objects.get(pk=accountId)
    # portfolio=Portfolio.objects.get(pk=account.portfolioAccount.pk)
    portfolio=Portfolio.objects.filter(portfolioAccount=account).first()
    # portfolios=Portfolio.objects.all()
    # portfolio=portfolios.first()
    return render(Request,'oneAccount.html',{'account':account,'portfolio':portfolio})


def showPortfolio(request):
    portfolios=Portfolio.objects.all()
    portfolio=portfolios.first()
    return render(request,'oneAccount.html',{'portfolio':portfolio})
def deleteAccount(Request,accountId):
    account=Account.objects.get(pk=accountId)
    account.delete()
    return render(Request,'accounts.html')
def deletePortfolio(Request,accountId):
    account=Account.objects.get(pk=accountId)
    portfolio=Portfolio.objects.get(portfolioAccount=account)
    print(account.pk)
    print(portfolio.pk)
    portfolio.delete()
    return render(Request,'oneAccount.html')
def newPortfolio(Request,accountId):
    account=Account.objects.get(pk=accountId)
    #form=newPortflioForm()
    if Request.method=='POST':
         who_is_you=Request.POST['whoareyou']
         what_does_you_do=Request.POST['wdyd']
         A_philosophy_statement=Request.POST['A_philosophy_statement']
         A_short_biography=Request.POST['A_short_biography']
         Professional_accomplishments=Request.POST['Professional_accomplishments']
         Awards_and_honors=Request.POST['Awards_and_honors']
         Transcripts_degrees_licenses_certifications=Request.POST['Transcripts_degrees_licenses_certifications']
         Volunteering_community_service=Request.POST['Volunteering_community_service']
         References_testimonials=Request.POST['References_testimonials']
         #print(A_short_biography)
         simpleuser=SimpleUser.objects.first()
         portfolio=Portfolio.objects.create(
          who_is_you=who_is_you, 
          what_does_you_do=what_does_you_do,
          A_philosophy_statement=A_philosophy_statement,
         A_short_biography=A_short_biography,
         Professional_accomplishments=Professional_accomplishments,
         Awards_and_honors=Awards_and_honors,
         Transcripts_degrees_licenses_certifications=Transcripts_degrees_licenses_certifications,
         Volunteering_community_service=Volunteering_community_service,
         References_testimonials=References_testimonials,
         portfolioAccount=Account.objects.get(pk=accountId)    
         )
         return redirect('showOneAccount',accountId)
    return render(Request,'newPortfolio.html',{'account':account})

def signup(request):
    if request.method=='POST':
     form=UserCreationForm(request.POST)
     if(len(request.POST['password'])>=8):
        if Account.objects.filter(password=request.POST['password']).exists():
            # print("password already exists")
            return error(request,"password already exists")
        else:
          simpleuser=SimpleUser.objects.create(
          name=request.POST['name']
         )
          account=Account.objects.create(
          login="".join([request.POST['name'],"@gmail.com"]), 
          password=request.POST['password']
          )

     else:
        # print("password too short sorry")
        return error(request,"password too short sorry")
     
     return redirect('home')
    return render(request,'signup.html')

def login(Request):
    if Request.method=='POST':
        login=Request.POST['login']
        password=Request.POST['password']
        # account=auth.authenticate(login=login,password=password)
        # if account is not None:
        #     auth.login(Request,account)
        #     # return redirect('home')
        #     # print("successfully loged")
        # else:
        #     return redirect('signup')
        if Account.objects.filter(login=login).exists():
            if Account.objects.filter(password=password).exists():
               primary=Account.objects.filter(password=password).values('accountId').first()['accountId']
               print("saha :)")
               print(str(primary)) 
            #    return redirect('showOneAccount',{'pk':primary})
            # return redirect("% url 'showOneAccount' primary %")
            # return redirect('home')
            return showOneAccount(Request,primary)
            # return redirect('showAccounts')
        else:
            print("5sara")
            return redirect('signup') 
    return render(Request,'login.html')

def adminlogin(request):
    if request.method=='POST':
        adminName=request.POST['name']
        adminId=request.POST['id']
        if Admin.objects.filter(name=adminName).exists():
            if Admin.objects.filter(userId=adminId).exists():
               primary=Admin.objects.filter(userId=adminId).values('userId').first()['userId']
               print("saha :)")
               print(str(primary)) 
            #    return redirect('showOneAccount',{'pk':primary})
            # return redirect("% url 'showOneAccount' primary %")
            # return redirect('home')
            return home(request)
            # return redirect('showAccounts')
        else:
            print("5sara") 
    return render(request,'adminLogin.html')
def updateColor(Request,accountId):
    account=Account.objects.get(pk=accountId)
    if Request.method=='POST':
     print("yemchi")
     color=Request.POST['color']
     
    return render(Request,'oneAccount.html',{'account':account})
def updateYourPortfolio(Request,accountId):
    account=Account.objects.get(pk=accountId)
    portfolio=Portfolio.objects.filter(portfolioAccount=account).first()
    if Request.method=='POST':
         portfolio.delete()
         who_is_you=Request.POST['whoareyou']
         what_does_you_do=Request.POST['wdyd']
         A_philosophy_statement=Request.POST['A_philosophy_statement']
         A_short_biography=Request.POST['A_short_biography']
         Professional_accomplishments=Request.POST['Professional_accomplishments']
         Awards_and_honors=Request.POST['Awards_and_honors']
         Transcripts_degrees_licenses_certifications=Request.POST['Transcripts_degrees_licenses_certifications']
         Volunteering_community_service=Request.POST['Volunteering_community_service']
         References_testimonials=Request.POST['References_testimonials']
         portfolio=Portfolio.objects.create(
          who_is_you=who_is_you, 
          what_does_you_do=what_does_you_do,
          A_philosophy_statement=A_philosophy_statement,
         A_short_biography=A_short_biography,
         Professional_accomplishments=Professional_accomplishments,
         Awards_and_honors=Awards_and_honors,
         Transcripts_degrees_licenses_certifications=Transcripts_degrees_licenses_certifications,
         Volunteering_community_service=Volunteering_community_service,
         References_testimonials=References_testimonials,
         portfolioAccount=Account.objects.get(pk=accountId)    
         ) 
    return render(Request,"updatePortfolio.html",{'account':account,'portfolio':portfolio})
def error(request,message):
    return render(request,"error.html",{'message':message})
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def home1(request):
    
    return render(request, 'core/authentificationsocial.html')

