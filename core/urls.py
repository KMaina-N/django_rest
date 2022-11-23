from django.urls import path, include, re_path

from rest_framework import routers
from .views import*
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from . import views
from core import views

router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'universities', UniversityViewSet)
router.register(r'accounts', UserView)

schema_view = get_schema_view(openapi.Info(
    title="Django REST API",	
    default_version='v1',
    description="Django REST API",
    terms_of_service="https://www.google.com/policies/terms/",
    contact=openapi.Contact(email="kev@example.com"),
    license=openapi.License(name="BSD License"),
), public=True)

urlpatterns = [
    path('index', views.index, name='index'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    re_path(r'^test/', include(router.urls)),
    re_path(r'^users/$', views.CreateUser),
    re_path(r'^users/(?P<pk>[0-9]+)/$', views.CreateUser),
    re_path(r'^create_universities/$', views.CreateUniversity),
    re_path(r'^create_universities/(?P<pk>[0-9]+)/$', views.CreateUniversity),
]

urlpatterns += router.urls