from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework import permissions, status
from sayts.pagination import LargeResultsSetPagination
from admin_panel.models import *
from sayts.serizalizers import *
from django.http import HttpResponse


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

#==================Flowers Views===================================
class FlowersAllSitesViews(APIView):
    pagination_class = LargeResultsSetPagination
    serializer_class = FlowersAllSerializers
    @property
    def paginator(self):
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        else:
            pass
        return self._paginator
    def paginate_queryset(self, queryset):
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset,self.request, view=self)
    def get_paginated_response(self, data):
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)
    def get(self,request,format=None):
        objects_list = Flowers.objects.all()
        page = self.paginate_queryset(objects_list)
        if page is not None:
            serializer = self.get_paginated_response(self.serializer_class(page, many=True).data)
        else:
            serializer = self.serializer_class(objects_list, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
class FlowersDeteileViews(APIView):
    def get(self,request,pk,format=None):
        objects_list = Flowers.objects.filter(id=pk)
        serializers = FlowersImagesSerizaliers(objects_list,many=True,context={'pk':pk})

        return Response(serializers.data,status=status.HTTP_200_OK)
    

def Flouvers(request):
    for item in FlowersImages.objects.all():
        x = item
    print(x)
    return HttpResponse()
