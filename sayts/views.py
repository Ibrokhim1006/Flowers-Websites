from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework import permissions, status
from admin_panel.models import *
from sayts.serizalizers import *


class CategoryAllSitesViews(APIView):
    def get(self,request,format=None):
        objects_list = Categoriya.objects.all()  
        serializers = CategoryAllSerializers(objects_list,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)
class SubCategoryAllSitesViews(APIView):
    def get(self,request,format=None):
        objects_list = SubCategoriya.objects.all()
        serializers = SubCategoryAllSerializers(objects_list,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)