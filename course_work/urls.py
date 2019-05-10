from django.contrib import admin
from django.urls import path
from entrant.views import index, add_anketa, show_all_anketa, exam
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_anketa/', add_anketa),
    path('show_all_anketa/', show_all_anketa),
    path('exam/', exam),
    path('', index),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)