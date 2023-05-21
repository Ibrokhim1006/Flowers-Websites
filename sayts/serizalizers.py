from rest_framework import serializers
from admin_panel.models import *


class CategoryAllSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categoriya
        fields = '__all__'
class SubCategoryAllSerializers(serializers.ModelSerializer):
    id_categoriya = CategoryAllSerializers(read_only=True)
    class Meta:
        model = SubCategoriya
        fields = '__all__'
