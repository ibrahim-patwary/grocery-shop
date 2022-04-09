
from django.urls import path
from .import views
#Django admin header customization 


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.home, name="home"),
    path('shop/',views.Shop, name="shop"),
    path('about/',views.About, name="about"),
    path('review/',views.Review, name="review"),
    path('blog/',views.Blog, name="blog"),
    path('contact/',views.Contact, name="contact"),
    path('Sing_up/', views.Sing_up, name="Sing_up"),
    path('singup', views.handle_singUp, name= "handle_singUp"),
    path('login', views.handle_login, name="handle_login"),
    path('logout', views.handle_logout, name="handle_logout"),
    path('data/',views.show_data,name='data'),  
]