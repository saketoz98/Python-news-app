from django.conf.urls import url
from basic_app import views


app_name = 'basic_app'
urlpatterns = [
    url(r'^$',views.categoryView,name="category"),
    url(r'^formPage/',views.formHandlerView,name="form"),
    url(r'^About/',views.about,name="about"),

]
