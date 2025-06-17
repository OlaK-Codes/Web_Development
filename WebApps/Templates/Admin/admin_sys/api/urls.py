#login token 
from api import views as api_views
from django.urls import path
#PROLONGATE TOKEN ACCESS VIA REFRESH
from rest_framework_simplejwt.views import TokenRefreshView   

urlpatterns = [
     #check token for access via login api form 
     path("user/token/", api_views.MyTokenObtainPairView.as_view()),
     #prolongate access via token refresh
     path("user/token/refresh/", TokenRefreshView.as_view()),
     #CREATE NWE USER VIA API FORM (registration form url)
     path("user/register/", api_views.RegisterView.as_view()),
     #ONE TIME PASSOWRD AUTO GENERATION AND RESET 
     path ("user/otp-password-reset/<email>/", api_views.PasswordResetEmailVerifyAPIView.as_view()),
     # CHANGE PASSWORD (NOT OTP)
     path ("user/password-change/", api_views.PasswordChangeAPIView.as_view())
]   