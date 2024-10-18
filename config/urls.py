from django.contrib import admin
from django.urls import path

from app.views import hello_view , age , order

urlpatterns = [
    path("hey/<name>", hello_view ),
    path("age-in/<end>/<birthyear>", age),
    path("order-total/<burgers>/<fries>/<drinks>", order),
    path('admin/', admin.site.urls),
]
