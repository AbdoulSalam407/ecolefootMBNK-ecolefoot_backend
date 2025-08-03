from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('logout/', LogoutView.as_view(next_page='https://ecolefoot-mbnk-ecolefoot-frontend.vercel.app/'), name='logout'),
    path('', admin.site.urls),
]
