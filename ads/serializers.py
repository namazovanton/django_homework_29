from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer

from ads.models import Ad, Category, Selection
from users.models import User
from users.serializers import UserSerializer, UserDetailSerializer


class AdSerializer(ModelSerializer):

    class Meta:
        fields = "__all__"
        model = Ad


class AdListSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field="username", queryset=User.objects.all())
    category = SlugRelatedField(slug_field="name", queryset=Category.objects.all())

    class Meta:
        fields = "__all__"
        model = Ad


class AdDetailSerializer(ModelSerializer):
    author = UserDetailSerializer()
    category = SlugRelatedField(slug_field="name", queryset=Category.objects.all())

    class Meta:
        fields = "__all__"
        model = Ad


class SelectionSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Selection


class SelectionDetailSerializer(ModelSerializer):
    items = AdSerializer(many=True)

    class Meta:
        fields = "__all__"
        model = Selection


class SelectionListSerializer(ModelSerializer):
    owner = SlugRelatedField(slug_field="username", queryset=User.objects.all())

    class Meta:
        fields = ["owner", "name"]
        model = Selection


class SelectionCreateSerializer(ModelSerializer):
    owner = SlugRelatedField(slug_field="username", read_only=True)

    def create(self, validated_data):
        request = self.context.det("request")
        validated_data["owner"] = request.user
        return super().create(validated_data)
    class Meta:
        fields = "__all__"
        model = Selection