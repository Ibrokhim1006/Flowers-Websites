from django.urls import path
from sayts.views import *

urlpatterns = [
    path('category_all_views/',CategoryAllSitesViews.as_view()),
    path('sub_category_all_views/',SubCategoryAllSitesViews.as_view())

]