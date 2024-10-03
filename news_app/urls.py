from django.urls import path
from .views import news_list, news_detail, HomePageView, UzbekPage, SportPage, AvtomabilPage, JahonPage, IqtisodPage


urlpatterns = [
    path('', HomePageView, name="homepage"),
    path("uzbeksitan/", UzbekPage, name="uzbekistan"),
    path("sport/", SportPage, name="sport"),
    path("avtomabil/", AvtomabilPage, name="avtomabil"),
    path("jahon/", JahonPage, name="jahon"),
    path("iqtisodiyot/", IqtisodPage, name="iqtisodiyot"),
    path("news/", news_list, name="news_all"),
    path("news/<int:id>/", news_detail, name="news_detail_page"),
]