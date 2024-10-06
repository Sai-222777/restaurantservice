from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('login',views.login_page,name="login_page"),
    path('register',views.register_page,name="register_page"),
    path('logout',views.logout_user,name='logout_user'), # logout not a page, but a function only
    path('menu',views.menu,name='menu_page'),
    path('debug-db/', views.debug_db, name='debug_db'),
]