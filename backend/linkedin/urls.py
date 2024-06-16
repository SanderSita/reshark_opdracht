from django.urls import path
from ninja import NinjaAPI
from .views import linkedin_router

api = NinjaAPI()

api.add_router("/linkedin", linkedin_router)

urlpatterns = [
    path("", api.urls),
]