from django.urls import path
from  .views import MemberView

urlpatterns= [

    path("api/member", MemberView.as_view()),

]