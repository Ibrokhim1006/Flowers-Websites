from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Categoriya(models.Model):
    title = models.CharField(max_length=250)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.title

class SubCategoriya(models.Model):
    title = models.CharField(max_length=250)
    id_categoriya = models.ForeignKey(Categoriya,on_delete=models.CASCADE,null=True,blank=True)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.title

# class SubCategoriyaTwo(models.Model):
#     title = models.CharField(max_length=250)
#     id_categroriya = models.ForeignKey(SubCategoriya,on_delete=models.CASCADE)
#     status = models.BooleanField(default=True)
#     def __str__(self) -> str:
#         return self.title    

class Flowers(models.Model):
    name = models.CharField(max_length=250)
    cotent = RichTextUploadingField(null=True,blank=True)
    rank = RichTextUploadingField(null=True,blank=True) # tarkibi
    price = models.CharField(max_length=250)
    like = models.SmallIntegerField(null=True,blank=True)
    iye = models.SmallIntegerField(null=True,blank=True)
    id_category = models.ForeignKey(Categoriya,on_delete=models.CASCADE,null=True,blank=True)
    id_sub_category = models.ForeignKey(SubCategoriya,on_delete=models.CASCADE,null=True,blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class FlowersImages(models.Model):
    id_flowers = models.ForeignKey(Flowers,on_delete=models.CASCADE,related_name='flowers')
    img = models.FileField(upload_to='flowers/',null=True,blank=True)
    def __str__(self):
        return "%s" % (self.id_flowers.name)


class FlowersCommentVideos(models.Model):
    id_flowers = models.ForeignKey(Flowers,on_delete=models.CASCADE,related_name='commit',null=True,blank=True)
    comment = models.ImageField(upload_to='commit/',null=True,blank=True)
    videos = models.FileField(upload_to='video/',null=True,blank=True)
    create_date = models.DateTimeField(auto_now_add=True)

class TypeDelivery(models.Model):
    title = models.CharField(max_length=250)
    price = models.CharField(max_length=250)
    def __str__(self):
        return self.title

class FlowersDelivery(models.Model):
    id_flowers = models.ManyToManyField(Flowers,blank=True)
    prcie = models.CharField(max_length=250,null=True,blank=True)
    id_type_delivery = models.ForeignKey(TypeDelivery,on_delete=models.CASCADE,null=True,blank=True)
    full_name = models.CharField(max_length=250,null=True,blank=True)
    phone = models.CharField(max_length=250,null=True,blank=True)
    full_name_payee = models.CharField(max_length=250,null=True,blank=True)
    phone_payee = models.CharField(max_length=250,null=True,blank=True)
    address_street_home = models.CharField(max_length=250,null=True,blank=True)
    address_addition = models.CharField(max_length=250,null=True,blank=True)
    date_delivery = models.DateField(null=True,blank=True)
    time_delivery = models.TimeField(null=True,blank=True)
    and_time = models.TimeField(null=True,blank=True)
    comment = models.TextField(null=True,blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.full_name

class Blogs(models.Model):
    title = models.CharField(max_length=250)
    content = RichTextUploadingField()
    img = models.FileField(upload_to='blog/',null=True,blank=True)
    eye = models.IntegerField(default=0,null=True,blank=True)
    like = models.IntegerField(default=0,null=True,blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class SeoCategory(models.Model):
    title = models.CharField(max_length=250)
    def __str__(self):
        return self.title
class SeoContent(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    id_seo = models.ForeignKey(SeoCategory,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    

class FormaSayts(models.Model):
    full_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name