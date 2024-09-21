from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.index, name='home'),
    path('shop/', views.shop, name='shop'),
    path('search/', views.search, name='search'),
    path('index', views.index, name='home1'),
    path('contact/', views.contact, name='contact'),
    path('product/<int:pk>', views.product, name='product'),
    path('maincat/<str:dummy>', views.maincategory, name='maincat'),
    path('subcat/<str:dummy>', views.subcategory, name='subcat'),
    path('mainsub/<str:dummy>/<str:parent>', views.mainsubcategory, name='mainsub'),
    path('login/', views.login_user, name="login"),
    path('update_user/', views.update_user, name="update_user"),
    path('update_info/', views.update_info, name="update_info"),
    path('update_password/', views.update_password, name="update_password"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),
]