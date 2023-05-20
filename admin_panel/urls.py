from django.urls import path
from admin_panel.views import *

urlpatterns = [
    path('user_sigin_in_views/',UserSiginInViews.as_view()),
    path('user_profiles_views/',UserProfilesViews.as_view()),
    #======================Categoriya And Sub Categoriya Urls==============
    path('categoriya_base_all_views/',CategoriyaBaseAllViews.as_view()),
    path('sub_categoriya_base_all_views/',SubCategoriyaBaseAllViews.as_view()),
    #======================Flowers Urls====================================
    path('flowers_base_all_views/',FlowersBaseAllViews.as_view()),
    path('flowers_base_crud_views/<int:pk>/',FlowersBaseCrudViews.as_view()),
    #======================Flowers Commit And Vidoe Urls==================
    path('flowers_video_commit_base_all_views/',FlowersVideoCommitBaseAllViews.as_view()),
    path('flowers_video_commit_crud_views/<int:pk>/',FlowersVideoCommitCrudViews.as_view()),
    #======================Flowers Delivery Urls============================
    path('flowers_delivery_base_all_views/',FlowersDeliveryBaseAllViews.as_view()),
    path('flowers_delivery_crud_views/<int:pk>/',FlowersDeliveryCrudViews.as_view()),

]   