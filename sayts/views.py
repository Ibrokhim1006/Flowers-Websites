from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework import permissions, status
from sayts.pagination import LargeResultsSetPagination
from rest_framework import generics
from rest_framework import filters
from admin_panel.models import *
from sayts.serizalizers import *
from admin_panel.serizalizers import *
from django.http import HttpResponse


class CategoryAllSitesViews(APIView):
    def get(self,request,format=None):
        objects_list = Categoriya.objects.all()  
        serializers = CategoryAllSerializers(objects_list,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)
class SubCategoryAllSitesViews(APIView):
    def get(self,request,pk,format=None):
        objects_list = SubCategoriya.objects.filter(id_categoriya__id=pk)
        serializers = SubCategoryAllSerializers(objects_list,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)

class FlowersCategoryDeteile(APIView):
    def get(self,request,pk,format=None):
        objects_list = Flowers.objects.filter(id_category__id=pk)
        serializers = FlowersAllSerializers(objects_list,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)
class FlowersSubCategoryDeteile(APIView):
    def get(self,request,pk,format=None):
        objects_list = Flowers.objects.filter(id_sub_category__id=pk)
        serializers = FlowersAllSerializers(objects_list,many=True)
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
        objects_list = Flowers.objects.all().order_by('-pk')
        page = self.paginate_queryset(objects_list)
        if page is not None:
            serializer = self.get_paginated_response(self.serializer_class(page, many=True).data)
        else:
            serializer = self.serializer_class(objects_list, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
class FlowersDeteileViews(APIView):
    def get(self,request,pk,format=None):
        objects_list = Flowers.objects.filter(id=pk)
        serializers = FlowersAllSerializers(objects_list,many=True,context={'pk':pk})

        return Response(serializers.data,status=status.HTTP_200_OK)
def Flouvers(request):
    for item in FlowersImages.objects.all():
        x = item
    print(x)
    return HttpResponse()
#====================================== Otziv Views ==================================
class CommitVidoesSitesViews(APIView):
    pagination_class = LargeResultsSetPagination
    serializer_class = CommitVidoesSerizalizers
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
        objects_list = FlowersCommentVideos.objects.all().order_by('-pk')
        page = self.paginate_queryset(objects_list)
        if page is not None:
            serializer = self.get_paginated_response(self.serializer_class(page, many=True).data)
        else:
            serializer = self.serializer_class(objects_list, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class FlowersDeliveryCategory(APIView):
    def get(self,request,format=None):
        objects_list =TypeDelivery.objects.all()
        serializers = TypeDeliverySerializers(objects_list,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)
class FlowersDeliverySitesViews(APIView):
    def post(self,request,format=None):
        serializers = FlowersDeliveryCrudSerializers(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

class BlogsAllSitesViews(APIView):
    pagination_class = LargeResultsSetPagination
    serializer_class = BlogAllBaseSerialiezers
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
        objects_list = Blogs.objects.all().order_by('-pk')
        page = self.paginate_queryset(objects_list)
        if page is not None:
            serializer = self.get_paginated_response(self.serializer_class(page, many=True).data)
        else:
            serializer = self.serializer_class(objects_list, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
class BlogsDeteilesSitesViews(APIView):
    def get(self,request,pk,format=None):
        objects_list = Blogs.objects.filter(id=pk)
        serializers = BlogAllBaseSerialiezers(objects_list,many=True)
        objects = Blogs.objects.filter(id=pk)[0]
        objects.eye=objects.eye+1
        objects.save(update_fields=['eye',])
        return Response(serializers.data,status=status.HTTP_200_OK)
    def put(self,request,pk,format=None):
        objects_list = Blogs.objects.filter(id=pk)[0]
        objects_list.like=objects_list.like+1
        objects_list.save(update_fields=['like',])
        return Response({'message':'like'},status=status.HTTP_200_OK)

class AllProductSearchView(generics.ListAPIView):
    queryset = Flowers.objects.all()
    serializer_class = FlowersAllSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['name','price']

class SeoAllSitesViews(APIView):
    def get(self,request,format=None):
        objects_list = Blogs.objects.all()
        serializers = SeoContentAllSerialiezers(objects_list,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)