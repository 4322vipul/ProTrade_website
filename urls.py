from django.urls import path
from .import views


urlpatterns=[path("login",views.login_view,name="login"),
             path("logout",views.logout_view,name="logout"),
             path("home",views.home,name="home"),
             path("buy",views.buy,name="buy"),
             path("sell",views.sell,name="sell"),
             path("swap",views.swap,name="swap"),
             path("successPage",views.successPage,name="successPage"),
             path("feedbackSuccessPage",views.feedbackSuccessPage,name="feedbackSuccessPage"),
             path("contacts",views.contacts,name="contacts"),]
             