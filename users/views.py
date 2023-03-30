from django.db.models import Count, Q
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from users.models import User, Location
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from users.serializers import UserSerializer, UserCreateSerializer, UserUpdateSerializer, UserListSerializer, \
    LocationSerializer


class UserPagination(PageNumberPagination):
    page_size = 4


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserListView(ListAPIView):
    queryset = User.objects.annotate(total_ads=Count("ad", filter=Q(ad__is_published=True))).order_by("username")
    serializer_class = UserListSerializer
    pagination_class = UserPagination


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer


class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


# @method_decorator(csrf_exempt, name='dispatch')
# class UserCreateView(CreateView):
#     model = User
#     fields = '__all__'
#
#     def post(self, request, *args, **kwargs):
#         data = json.loads(request.body)
#
#         locations = data.pop("locations")
#         user = User.objects.create(**data)
#         for loc_name in locations:
#             loc, created = Location.objects.get_or_create(name=loc_name)
#             user.location.add(loc)
#
#         return JsonResponse({"id": user.id,
#                              "first_name": user.first_name,
#                              "last_name": user.last_name,
#                              "username": user.username,
#                              "role": user.role,
#                              "age": user.age,
#                              "location": [loc.name for loc in user.location.all()]})
#
#
# @method_decorator(csrf_exempt, name='dispatch')
# class UserUpdateView(UpdateView):
#     model = User
#     fields = '__all__'
#
#     def patch(self, request, *args, **kwargs):
#         super().post(request, *args, **kwargs)
#         data = json.loads(request.body)
#
#         if "first_name" in data:
#             self.object.first_name = data.get("first_name")
#         if "last_name" in data:
#             self.object.last_name = data.get("last_name")
#         if "username" in data:
#             self.object.username = data.get("username")
#         if "age" in data:
#             self.object.age = data.get("age")
#         if "locations" in data:
#             self.object.location.clear()
#             for loc_name in data.get("locations"):
#                 loc, created = Location.objects.get_or_create(name=loc_name)
#                 self.object.location.add(loc)
#
#         self.object.save()
#         return JsonResponse({"id": self.object.id,
#                              "first_name": self.object.first_name,
#                              "last_name": self.object.last_name,
#                              "username": self.object.username,
#                              "role": self.object.role,
#                              "age": self.object.age,
#                              "location": [loc.name for loc in self.object.location.all()]})