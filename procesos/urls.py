from rest_framework import routers
from django.urls import path, include
from procesos import views
from rest_framework.documentation import include_docs_urls


router = routers.DefaultRouter()
router.register(r'procesos', views.ProcesosViews,'procesos')

urlpatterns =  [
    path('api/v1/', include(router.urls)),
    path('docs/', include_docs_urls(title="proceso docs"))
]