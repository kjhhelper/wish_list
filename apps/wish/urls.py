from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.index),
    url(r'^register$',views.register),
    url(r'^dashboard$',views.dashboard),
    url(r'^itemprocess$',views.itemprocess),
    url(r'^item$',views.item),
    url(r'^wishprocess$',views.wishlistprocess),
    url(r'^wishlist$',views.wishlist)
]
