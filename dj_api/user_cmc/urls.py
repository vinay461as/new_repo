from django.urls import path
from  .views import MemberView

urlpatterns= [

    path("api", MemberView.as_view()),

]
