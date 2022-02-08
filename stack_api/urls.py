from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from stack_api import settings
from main.views import ProblemViewsSet

router = DefaultRouter()
router.register('problems', ProblemViewsSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
