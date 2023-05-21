from rest_framework.response import Response
from django.contrib.auth import authenticate,logout
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404
from admin_panel.renderers import UserRenderers
from rest_framework.pagination import PageNumberPagination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.parsers import MultiPartParser, FormParser
from admin_panel.pagination import *
from admin_panel.serizalizers import *
from admin_panel.models import *


def get_token_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'accsess':str(refresh.access_token)
    }

class UserSiginInViews(APIView):
    render_classes = [UserRenderers]
    def post(self,request,format=None):
        serializers = UserSiginInSerizalizers(data=request.data, partial=True)
        if serializers.is_valid(raise_exception=True):
            username = request.data['username']
            password = request.data['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                tokens = get_token_for_user(user)
                return Response({'token':tokens,'message':'Welcome to the system'},status=status.HTTP_200_OK)
            else:
                return Response({'error':{'none_filed_error':['This user is not available to the system']}},status=status.HTTP_404_NOT_FOUND)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
class UserProfilesViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    def get(self,request,format=None):  
        serializer = UserPorfilesSerializers(request.user)
        return Response(serializer.data,status=status.HTTP_200_OK)

#=====================Categori and Sub Categoriya Views===================================
class CategoriyaBaseAllViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    def get(self,request,format=None):
        objects_list = Categoriya.objects.all()
        # page_number = self.request.query_params.get('page_number ', 2)
        # page_size = self.request.query_params.get('page_size ', 1)

        # paginator = Paginator(objects_list , page_size)
        # paginator.page(page_number)
        serializer = CategoriyaAllSerializers(objects_list,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request,format=None):
        serializers = CategoriyaCrudSerializers(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response({'message':'Create Sucsess'},status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

class SubCategoriyaBaseAllViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    def get(self,request,format=None):
        objects_list = SubCategoriya.objects.all()
        serializer = SubCategoriyaAllSerializers(objects_list,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
#===============================Flowers Views==========================================
class FlowersBaseAllViews(APIView,PageNumberPagination):
    parser_class = [MultiPartParser, FormParser]
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    page_size = 1

    def get(self,request,format=None):
        objects_list = Flowers.objects.all()
        result = self.paginate_queryset(objects_list,request,view=self)
        serializers = FlowersBaseAllSerializers(result,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)
    def post(self,request,format=None):
        serializers = FlowersBaseCruderializers(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response({'message':'Create Sucsess'},status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
class FlowersBaseCrudViews(APIView):
    parser_class = [MultiPartParser, FormParser]
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    def get(self,request,pk,format=None):
        objects_list = Flowers.objects.filter(id=pk)
        # for item in objects_list:
        #     x = item.id
        # objects_comment = FlowersCommentVideos.objects.filter(id_flowers__id=item.id)
        # objects_img = FlowersImages.objects.filter(id_flowers_id=x)
        # serizaliers_commit = FlowersCommitVideoBaseSerializers(objects_comment,many=True)
        # serizalizer_images = FlowersImagesAllSerizaliers(objects_img,many=True)
        seriz = FlowersBaseAllSerializers(objects_list,many=True)
        return Response(seriz.data,status=status.HTTP_200_OK)
    def put(self,request,pk,format=None):
        serializers = FlowersBaseCruderializers(instance=Flowers.objects.filter(id=pk)[0],data=request.data,partial =True)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response({'message':"success update"},status=status.HTTP_200_OK)
        return Response({'error':'update error data'},status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk,format=None):
        objects_get = Flowers.objects.get(id=pk)
        objects_get.delete()
        return Response({'message':"Delete success"},status=status.HTTP_200_OK)
# class FlowersImagesPostViews(APIView):
#     render_classes = [UserRenderers]
#     perrmisson_class = [IsAuthenticated]
#     def get(self,request,format=None):
#         objects_list = Flowers.objects.all()
#         serializer = FlowersBaseAllSerializers(objects_list,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
#     def post(self,request,format=None):
#         serializers = FlowersImagesCrudSerializers(data=request.data)
#         if serializers.is_valid(raise_exception=True):
#             serializers.save()
#             return Response({'message':'Create Sucsess'},status=status.HTTP_201_CREATED)
#         return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

#===============================Flowers Commit And Videos Views==========================================
class FlowersVideoCommitBaseAllViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    def get(self,request,format=None):
        objects_list = FlowersCommentVideos.objects.all()
        serializer = FlowersCommitVideoBaseSerializers(objects_list,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request,format=None):
        serializers = FlowersCommitVideoCrudSerializers(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save(comment = request.data.get('comment'))
            return Response({'message':'Create Sucsess'},status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
class FlowersVideoCommitCrudViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    def get(self,request,pk,format=None):
        objects_list = FlowersCommentVideos.objects.all()
        serializer = FlowersCommitVideoBaseSerializers(objects_list,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def put(self,request,pk,format=None):
        serializers = FlowersCommitVideoCrudSerializers(instance=FlowersCommentVideos.objects.filter(id=pk)[0],data=request.data,partial =True)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response({'message':"success update"},status=status.HTTP_200_OK)
        return Response({'error':'update error data'},status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk,format=None):
        objects_get = FlowersCommentVideos.objects.get(id=pk)
        objects_get.delete()
        return Response({'message':"Delete success"},status=status.HTTP_200_OK)
#=============================Flowers Delivery Views===========================
class FlowersDeliveryBaseAllViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    def get(self,request,format=None):
        objects_list = FlowersDelivery.objects.all()
        serializer = FlowersDeliveryBaseSerializers(objects_list,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request,format=None):
        serializers = FlowersDeliveryCrudSerializers(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response({'message':'Create Sucsess'},status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
class FlowersDeliveryCrudViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    def get(self,request,pk,format=None):
        objects_list = FlowersDelivery.objects.filter(id=pk)
        serializer = FlowersDeliveryBaseSerializers(objects_list,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def delete(self,request,pk,format=None):
        objects_get = FlowersDelivery.objects.get(id=pk)
        objects_get.delete()
        return Response({'message':"Delete success"},status=status.HTTP_200_OK)

#=============================Blogs Views===========================
class BlogsAllViews(generics.ListAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogAllBaseSerialiezers
    pagination_class = LargeResultsSetPagination
class BlogsBaseAllViews(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]
    def get(self,request,format=None):
        objects_list = Blogs.objects.all()
        serializers = BlogAllBaseSerialiezers(objects_list,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)
    def post(self,request,format=None):
        serializers = FlowersDeliveryCrudSerializers(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response({'message':'Create Sucsess'},status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)