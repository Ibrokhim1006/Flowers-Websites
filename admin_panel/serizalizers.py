from django.contrib.auth.models import User,Group
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from admin_panel.models import *


class UserSiginInSerizalizers(serializers.ModelSerializer):
    username = serializers.CharField(max_length=250)
    class Meta:
        model = User
        fields = ['username','password',]
class UserPorfilesSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','first_name','last_name',]

#===================Categoria And Sub Categoriya Serializers=====================
class CategoriyaAllSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categoriya
        fields = '__all__'
class CategoriyaCrudSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categoriya
        fields = ['id','title','img','status',]
    def create(self, validated_data):
        return Categoriya.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.img = validated_data.get('img',instance.img)
        instance.status = validated_data.get('status',instance.status)
        instance.save() 
        return instance

class SubCategoriyaAllSerializers(serializers.ModelSerializer):
    id_categoriya = CategoriyaAllSerializers(read_only=True)
    class Meta:
        model = SubCategoriya
        fields = ['id','title','id_categoriya','status',]
class CategoriyaAllSerialize(serializers.ModelSerializer):
    class Meta:
        model = Categoriya
        fields = '__all__'        
class SubCategoriyaCrudSerializers(serializers.ModelSerializer):
    # id_categoriya = CategoriyaAllSerialize(read_only=True)
    # roll_number = serializers.IntegerField()  
    class Meta:
        model = SubCategoriya
        fields = ['id','title','id_categoriya','status',]
    def create(self, validated_data):
        return SubCategoriya.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.id_categoriya = validated_data.get('id_categoriya',instance.id_categoriya)
        instance.status = validated_data.get('status',instance.status)
        instance.save() 
        return instance
#========================Flowers Serializers=========================
class FlowersImagesSer(serializers.ModelSerializer):
    class Meta:
        model = FlowersImages
        fields = '__all__'
class FlowersBaseAllSerializers(serializers.ModelSerializer):
    id_category = CategoriyaAllSerializers(read_only=True)    
    id_sub_category = SubCategoriyaAllSerializers(read_only=True)
    flowers = FlowersImagesSer(many=True,read_only=True)
    class Meta:
        model = Flowers
        fields = ('id','name','cotent','rank','price','upa','con','like','iye','id_category','id_sub_category','create_date','flowers')

class FlowersBaseCruderializers(serializers.ModelSerializer):
    # id_category = CategoriyaAllSerializers(read_only=True)
    # id_sub_category = SubCategoriyaAllSerializers(read_only=True)
    # flowers= FlowersImagesSer(many=True, read_only = True)
    img = serializers.ListField(
        child = serializers.ImageField(max_length = 1000000, allow_empty_file = False, use_url = False),
        write_only=True)
    class Meta:
        model = Flowers
        fields = ['id','name','cotent','rank','price','upa','con','like','iye','id_category','id_sub_category','img']
    def create(self, validated_data):
        img = validated_data.pop('img')
        flowers = Flowers.objects.create(**validated_data)
        for item in img:
            images = FlowersImages.objects.create(id_flowers=flowers,img=item)
            images.save()
        return flowers
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.cotent = validated_data.get('cotent',instance.cotent)
        instance.price = validated_data.get('price',instance.price)
        instance.rank = validated_data.get('rank',instance.rank)
        instance.upa = validated_data.get('upa',instance.upa)
        instance.con = validated_data.get('con', instance.con)
        instance.like = validated_data.get('like',instance.like)
        instance.iye = validated_data.get('iye',instance.iye)
        instance.id_sub_category = validated_data.get('id_sub_category',instance.id_sub_category)
        instance.id_category = validated_data.get('id_category',instance.id_category)
        instance.save() 
        return instance
class FlowersImagesAllSerizaliers(serializers.ModelSerializer):
    id_flowers = FlowersBaseAllSerializers(read_only=True)
    class Meta:
        model = FlowersImages
        fields = ['id','id_flowers','img']
class FlowersImagesCrudSerializers(serializers.ModelSerializer):
    # id_flowers = FlowersBaseAllSerializers(read_only=True)

    class Meta:
        model = FlowersImages
        fields = ['id','id_flowers','img']
    def create(self, validated_data):
        return FlowersImages.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.id_flowers = validated_data.get('id_flowers',instance.id_flowers)
        instance.img = validated_data.get('img',instance.img)
        instance.save() 
        return instance
        
#=======================Flowers Commit And Videos Serizalizers================
class FlowersCommitVideoBaseSerializers(serializers.ModelSerializer):
    id_flowers = FlowersBaseAllSerializers(read_only=True)
    class Meta:
        model = FlowersCommentVideos
        fields = ['id','id_flowers','comment','create_date']
class FlowersCommitVideoCrudSerializers(serializers.ModelSerializer):
    # id_flowers = FlowersBaseAllSerializers(read_only=True)
    class Meta:
        model = FlowersCommentVideos
        fields = ['id','id_flowers','comment','create_date']
    def create(self, validated_data):
        return FlowersCommentVideos.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.id_flowers = validated_data.get('id_flowers',instance.id_flowers)
        instance.comment = validated_data.get('comment',instance.comment)
        instance.save() 
        return instance

#=======================Flowers Delivery Serizalizers================
class TypeDeliverySerializers(serializers.ModelSerializer):
    class Meta:
        model = TypeDelivery
        fields = '__all__'

class SizeSerializers(serializers.ModelSerializer):
    class Meta:
        model = SizeFlow
        fields = '__all__'

class FlowersDeliveryBaseSerializers(serializers.ModelSerializer):
    id_flowers = FlowersBaseAllSerializers(read_only=True,many=True)
    id_type_delivery = TypeDeliverySerializers(read_only=True)
    id_size = SizeSerializers(read_only=True)
    class Meta:
        model = FlowersDelivery
        fields = ['id','id_flowers','prcie','id_size','id_type_delivery','full_name','phone','full_name_payee','phone_payee','address_street_home','address_addition','date_delivery','time_delivery','and_time','comment','create_date',]

class FlowersDeliveryCrudSerializers(serializers.ModelSerializer): 
    # id_flowers = FlowersBaseAllSerializers(read_only=True)
    # id_type_delivery = TypeDeliverySerializers(read_only=True)
    class Meta:
        model = FlowersDelivery
        fields = ['id', 'fowers']
    def create(self, validated_data):
        """News Create Function"""
        return FlowersDelivery.objects.create(**validated_data)
    # def update(self, instance, validated_data):
    #     instance.id_flowers = validated_data.get('id_flowers',instance.id_flowers)
    #     instance.comment = validated_data.get('comment',instance.comment)
    #     instance.videos = validated_data.get('videos',instance.videos)
    #     instance.save() 
    #     return instance


#=======================Blogs Serizalizers================
class BlogAllBaseSerialiezers(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields = "__all__"
class BlogCrudBaseSerialiezers(serializers.ModelSerializer):
    img = serializers.ImageField(max_length=None, allow_empty_file=False,allow_null=False,use_url=False,required=False)
    class Meta:
        model = Blogs
        fields = "__all__"
    def create(self, validated_data):
        return Blogs.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.content = validated_data.get('content',instance.content)
        if instance.img == None:
            instance.img = self.context.get('img')
        else:
            instance.img = validated_data.get('img',instance.img)
        instance.eye = validated_data.get('eye',instance.eye)
        instance.like = validated_data.get('like',instance.like)
        instance.create_date = validated_data.get('create_date',instance.create_date)
        instance.save() 
        return instance

#=============================SEO Serializers==================================================
class SeoCategoryAllSerialiezers(serializers.ModelSerializer):
    class Meta:
        model = SeoCategory
        fields = "__all__"

class SeoContentAllSerialiezers(serializers.ModelSerializer):
    id_seo = SeoCategoryAllSerialiezers(read_only=True)
    class Meta:
        model = SeoContent
        fields = "__all__"

class SeoContentCrudSerialiezers(serializers.ModelSerializer):
    # id_seo = SeoCategoryAllSerialiezers(read_only=True)

    class Meta:
        model = SeoContent
        fields = ['id','title','content','id_seo']
    def create(self, validated_data):
        return SeoContent.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.content = validated_data.get('content',instance.content)
        instance.id_seo = validated_data.get('id_seo',instance.id_seo)
        instance.save() 
        return instance


class FormasAllSerizalisers(serializers.ModelSerializer):
    class Meta:
        model = FormaSayts
        fields = '__all__'

class FormaCreateSerizliers(serializers.ModelSerializer):
    class Meta:
        model = FormaSayts
        fields = '__all__'
    def create(self, validated_data):
        return FormaSayts.objects.create(**validated_data)

