from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


from .views import Profile, GoogleCallbackView, GoogleLoginView
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('profile/', Profile.as_view(), name="user_profile"),

    path('google/login/', GoogleLoginView.as_view(), name="google-view"),
    path('google/callback/', GoogleCallbackView.as_view(), name="callback"),

]