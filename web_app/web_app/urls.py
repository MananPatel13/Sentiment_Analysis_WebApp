# from django.contrib import admin
# from django.urls import path,include
# from myapp.views import register, user_login
# from myapp.views import home

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('register/', register, name='register'),
#     path('login/', user_login, name='login'),
# ]

from django.contrib import admin
from django.urls import path, include
from myapp import views as user_view
from django.contrib.auth import views as auth
from .router import router
from rest_framework.authtoken import views
from api.views import SentimentAnalysisView
# from .router import router
# from rest_framework.authtoken import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/sentiment-analysis/', SentimentAnalysisView.as_view(), name='sentiment_analysis'),
    ######### api path ##########################

    # path('api/', include(router.urls)),
    # path('api-token-auth/', views.obtain_auth_token, name='api-tokn-auth'),

    #####user related path##########################
    path('', include('myapp.urls')),
    path('login/', user_view.Login, name='login'),
    path('logout/', auth.LogoutView.as_view(template_name='user/index.html'), name='logout'),
    path('register/', user_view.register, name='register'),

]