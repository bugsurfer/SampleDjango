from django.conf.urls import url

from User.views import UserProfile, UserBalance

urlpatterns = [
    url(r'balance', UserBalance),
    url(r'', UserProfile.as_view()),
]
