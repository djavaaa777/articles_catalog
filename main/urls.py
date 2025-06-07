from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.main,name='main'),
    path('about', views.about,name='about'),
    path('register', views.register,name='register'),
    path('login/', auth_views.LoginView.as_view(
        template_name='main/login.html',
        redirect_authenticated_user=True,
        next_page='main'  
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='main'), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name='article_detail'),
    path('reviews/', views.review, name='reviews'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
