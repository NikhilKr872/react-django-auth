from django.urls import URLPattern, path
from .views import getRoutes,MyTokenObtainPairView,getNotes
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns=[ 
    path('',getRoutes),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('notes/',getNotes)
]