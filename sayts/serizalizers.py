from rest_framework import serializers
from admin_panel.models import *


class CategoryAllSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categoriya
        fields = "__all__"


class SubCategoryAllSerializers(serializers.ModelSerializer):
    id_categoriya = CategoryAllSerializers(read_only=True)

    class Meta:
        model = SubCategoriya
        fields = "__all__"


# =========================== Flowers Serilaziers ======================
class CategoryFlowers(serializers.ModelSerializer):
    class Meta:
        model = Categoriya
        fields = "__all__"


class SubCategoryFlowers(serializers.ModelSerializer):
    class Meta:
        model = SubCategoriya
        fields = "__all__"


class ImgFlowers(serializers.ModelSerializer):
    class Meta:
        model = FlowersImages
        fields = "__all__"


class CommitVideoSer(serializers.ModelSerializer):
    class Meta:
        model = FlowersCommentVideos
        fields = "__all__"


class SizesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'


class PriceSerializers(serializers.ModelSerializer):
    size = SizesSerializers(read_only=True)
    class Meta:
        model = Price
        fields = '__all__'


class FlowersAllSerializers(serializers.ModelSerializer):
    id_category = CategoryFlowers(read_only=True)
    id_sub_category = SubCategoryFlowers(read_only=True)
    flowers = ImgFlowers(many=True, read_only=True)
    commit = CommitVideoSer(many=True, read_only=True)
    prices = PriceSerializers(many=True,read_only=True)

    class Meta:
        model = Flowers
        fields = "__all__"


class FlowersImagesSerizaliers(serializers.ModelSerializer):
    # id_flowers = FlowersAllSerializers(read_only=True)
    class Meta:
        model = Flowers
        fields = "__all__"

    def get_attempt(self, obj):
        quiztaker = FlowersImages.objects.filter(
            id_flowers__id=self.context.get("id"), quiz=obj
        )
        for attempt in quiztaker:
            print(attempt)
            attempt_number = attempt.id
        return attempt_number


class CommitVidoesSerizalizers(serializers.ModelSerializer):
    id_flowers = FlowersAllSerializers()

    class Meta:
        model = FlowersCommentVideos
        fields = "__all__"
