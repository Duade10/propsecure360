from django.urls import path

from . import views

urlpatterns = [
    path("create", views.CreateUserRequest.as_view()),
    path("detail/<str:user_request_id>", views.GetUserRequest.as_view()),
    path("list", views.ListUserRequest.as_view()),
    path("list-all", views.ListAllUserRequest.as_view()),
    path("create-quotation", views.CreateQuotation.as_view()),
    path("get-quotation/<str:quotation_id>", views.GetQuotation.as_view()),
]
