from django.urls import path
from sayts.views import *

urlpatterns = [
    path('category_all_views/',CategoryAllSitesViews.as_view()),
    path('sub_category_all_views/<int:pk>/',SubCategoryAllSitesViews.as_view()),
    #========================= FLowers Urls ===========================
    path('flowers_all_sites_views/',FlowersAllSitesViews.as_view()),
    path('flowers_category_deteile/<int:pk>/',FlowersCategoryDeteile.as_view()),
    path('flowers_sub_category_deteile/<int:pk>/',FlowersSubCategoryDeteile.as_view()),
    path('Flouvers/',Flouvers),
    path('flowers_deteile_views/<int:pk>/',FlowersDeteileViews.as_view()),

    path('commit_vidoes_sites_views/',CommitVidoesSitesViews.as_view()),

    path('flowers_delivery_category/',FlowersDeliveryCategory.as_view()),
    path('flowers_delivery_sites_views/',FlowersDeliverySitesViews.as_view()),
    path('blogs_deteiles_sites_views/<int:pk>/',BlogsDeteilesSitesViews.as_view()),

    path('blogs_all_sites_views/',BlogsAllSitesViews.as_view()),
    path('blogs_deteiles_sites_views/<int:pk>/',BlogsDeteilesSitesViews.as_view()),
    path('AllProductSearchView/',AllProductSearchView.as_view()),

    path('seo_all_sites_views/',SeoAllSitesViews.as_view()),

    path('forma_post_sites_views/',FormaPostSitesViews.as_view())

]