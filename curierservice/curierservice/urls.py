from django.contrib import admin
from django.urls import path
from curier import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.user_login, name="user_login"),
    path('signup/', views.signup1, name="signup"),
    path('home/', views.home, name="home"),
    path('edit_parcel/<int:pid>/', views.edit_parcel, name="edit_parcel"),
    path('assign_status/<int:pid>/', views.assign_status, name="assign_status"),
    path('Logout/', views.Logout, name="Logout"),
    path('delete_history/<int:pid>/', views.delete_history, name="delete_history"),
    path('all_accept_parcel/', views.all_accept_parcel, name="all_accept_parcel"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
