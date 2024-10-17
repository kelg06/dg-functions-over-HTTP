from django.contrib import admin
from django.urls import path

from app.views import hello_view , age , order

urlpatterns = [
    path("Hey/<name>/", hello_view ),
    path("age-in/<end>/<birthyear>", age),
    path("total/<burgers>/<fries>/<drinks>", order),
    path('admin/', admin.site.urls),
]
