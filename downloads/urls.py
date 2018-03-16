from django.conf.urls import url,include

urlpatterns = [
    url(r'^api/',include('downloads.api.urls')),
]