from django.contrib import admin
from django.urls import include, path

"""
path fonctionne ainsi => path('route/', view)
"""
urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
