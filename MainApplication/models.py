from django.db import models




class User(models.Model):
     userId=models.IntegerField(primary_key=True,null=False)
     name=models.CharField(max_length=50)
     
     class Meta:
        abstract=True
    

class SimpleUser(User):
    def __str__(self):
       return self.name
    class Meta:
         verbose_name="utilisateur"

class Admin(User):
    adminCheck=models.BooleanField(default=True)
    class Meta:
         verbose_name="admin"
class Account(models.Model):
    accountId=models.IntegerField(primary_key=True,null=False)
    login=models.EmailField(max_length=50)
    password=models.CharField(max_length=15,null=False,blank=False)
    color=models.CharField(max_length=15,null=True,blank=True)
    userAccount=models.OneToOneField(SimpleUser,on_delete=models.CASCADE, null=True)
    def __str__(self):
       return self.login
    class Meta:
           verbose_name="compte"
class Portfolio(models.Model):
   who_is_you=models.TextField(max_length=1000,null=True,blank=True)
   what_does_you_do=models.TextField(max_length=1000,null=True,blank=True)
   career_summary=models.TextField(max_length=1000,null=True,blank=True)
   A_philosophy_statement=models.TextField(max_length=1000,null=True,blank=True)
   A_short_biography=models.TextField(max_length=1000,null=True,blank=True)
   Professional_accomplishments=models.TextField(max_length=1000,null=True,blank=True)
   Awards_and_honors=models.TextField(max_length=1000,null=True,blank=True)
   Transcripts_degrees_licenses_certifications=models.TextField(max_length=1000,null=True,blank=True)
   Volunteering_community_service=models.TextField(max_length=1000,null=True,blank=True)
   References_testimonials=models.TextField(max_length=1000,null=True,blank=True)

   portfolioAccount=models.OneToOneField(Account,on_delete=models.CASCADE,null=True)
   def __str__(self):
       return " ".join(["porfolio of ",str(self.portfolioAccount)])

   class Meta:
        verbose_name="portfeuille"

    







