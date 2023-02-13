from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/v1/', include('user.urls')),
                  path('api/v1/', include('quiz.urls')),
                  path('api/v1/', include('battle.urls')),
                  path('api/v1/', include('universities.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
