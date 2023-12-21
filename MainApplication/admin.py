from django.contrib import admin
from .models import Portfolio,Account,SimpleUser,Admin
# Register your models here.
admin.site.register(Portfolio)
# admin.site.register(User)
admin.site.register(Account)
admin.site.register(Admin)
admin.site.register(SimpleUser)
