# """shop URL Configuration
#
# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/3.0/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
#


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('authentication.urls')),
    path('', include('frontend.urls')),
    path('showcase/', include('showcase.urls'))
]
# #
# # from rest_framework import routers
# #
# # router = routers.SimpleRouter()
# # urlpatterns = router.urls
#
# from django.contrib import admin
# from django.urls import path, include
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )
#
#
# urlpatterns = [
#    #  path('admin/', admin.site.urls),
#    #  path(r'^users/', include('accounts.urls')),
#    #  path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#    #  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#    #  path('', include('django.contrib.auth.urls')),
#    # # path('api/', include('article.urls')),
#     path('admin/', admin.site.urls),
#
#     # path to djoser end points
#     path('auth/', include('djoser.urls')),
#     path('auth/', include('djoser.urls.jwt')),
#
#     # path to our account's app endpoints
#   #  path("api/accounts/", include("accounts.urls"))
# ]
#
#
#
