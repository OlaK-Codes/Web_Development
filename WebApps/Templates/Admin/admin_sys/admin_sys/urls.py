"""
URL configuration for admin_sys project.

The `urlpatterns` list routes URLs to view. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function view
    1. Add an import:  from my_app import view
    2. Add a URL to urlpatterns:  path('', view.home, name='home')
Class-based view
    1. Add an import:  from other_app.view import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django .conf import settings
#to create own admin for cms
from CMS.admin import cms_site
# to create api documentation
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title = "AUTH API",
        default_version = "v1",
        description = "This is the API documentation for User Auth API project",
        #Create your own Terms of Service page on your website or app.
        terms_of_service ="https://yourdomain.com/terms",
        contact = openapi.Contact(email = "test@test.com"),
        license = openapi.License(name = 'BSD License'),
    ),
        public = True,
        #allows any request (authenticated or not).
        permission_classes = [permissions.AllowAny],
    )


urlpatterns = [
    #Admin Auth
    path('my-unique-admin/', admin.site.urls),
    #to create own url for admin in cms
    path('cms-admin/', cms_site.urls),
    #captha
    #path('captcha/', include('captcha.urls')),
    # csv file data into admin db
    path('datawizard/', include('data_wizard.urls')),
    # API - login token serialisation
    path("api/v1/", include("api.urls")),
    # Docs paths
    path("swagger<format>/", schema_view.without_ui(cache_timeout = 0),name ='schema-json'),
    path('', schema_view.with_ui('swagger',cache_timeout = 0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',cache_timeout = 0), name='schema-redoc'),
    
] +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
