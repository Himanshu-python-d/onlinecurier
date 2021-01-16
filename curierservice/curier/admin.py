from django.contrib import admin
from .models import Signup, CurierList
# Register your models here.

@admin.register(Signup)
class SignupAdmin(admin.ModelAdmin):
    class Meta:
        model = Signup
        fields = '__all__'

@admin.register(CurierList)
class CurierListAdmin(admin.ModelAdmin):
    class Meta:
        model = CurierList
        fields = '__all__'
