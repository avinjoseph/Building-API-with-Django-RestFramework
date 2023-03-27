from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    # TokenRefreshView,
)


urlpatterns = [
    path('',views.endpoints),
    path('advocates/',views.advocate_list),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # path('advocates/<str:username>/',views.advocate_detail)
    path('advocates/<str:username>/',views.AdvocateDetails.as_view()),

    path('companies/',views.company_details),
]
