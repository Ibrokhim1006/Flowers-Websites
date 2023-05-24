from django.urls import path
from sayts.views import *

urlpatterns = [
    path('category_all_views/',CategoryAllSitesViews.as_view()),
    path('sub_category_all_views/',SubCategoryAllSitesViews.as_view()),
    #========================= FLowers Urls ===========================
    path('flowers_all_sites_views/',FlowersAllSitesViews.as_view()),
    path('Flouvers/',Flouvers),
    path('flowers_deteile_views/<int:pk>/',FlowersDeteileViews.as_view()),

]