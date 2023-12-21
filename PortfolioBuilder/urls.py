"""PortfolioBuilder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from MainApplication import views
# from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',views.home,name='showAccounts'),
    path('accounts/<int:accountId>/',views.showOneAccount,name='showOneAccount'),
    path('accounts/<int:accountId>/delete',views.deleteAccount,name='deleteAccount'),
    path('accounts/<int:accountId>/new',views.newPortfolio,name="newPortfolio"),
    path('login/<int:accountId>/new',views.newPortfolio,name="newPortfolio"),
    path('login/<int:accountId>/update',views.updateYourPortfolio,name="updatePortfolio"),
    path('login/admin/accounts',views.home,name='showAccounts'),
    path('accounts/<int:accountId>/deletePortfolio',views.deletePortfolio,name="deletePortfolio"),
    path('portfolios/',views.showAllPortfolios,name="showAllPortfolios"),
    # path('api-auth',include('rest_framework.urls')),
    path('signup/',views.signup,name='signup'),
    path('',views.acceuil,name="home"),
    path('login/',views.login,name="login"),
    path('portfolio',views.showPortfolio),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('login/<int:accountId>/',views.showOneAccount,name='showOneAccount'),
    path('login/<int:accountId>/deletePortfolio',views.deletePortfolio,name="deletePortfolio"),
    path('login/<int:accountId>/delete',views.deleteAccount,name='deleteAccount'),
    path('login/admin',views.adminlogin),
    path('login/<int:accountId>/updateColor',views.updateColor),
    # path('api/token/',TokenObtainPairView.as_view()),
    # path('api/token/refresh/',TokenRefreshView.as_view())
]
