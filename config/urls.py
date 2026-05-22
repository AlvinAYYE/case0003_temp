from django.http import HttpRequest, HttpResponse
from django.urls import path


def health(request: HttpRequest) -> HttpResponse:
    return HttpResponse("ok")

urlpatterns = [
    path("health/", health, name="health"),
]
