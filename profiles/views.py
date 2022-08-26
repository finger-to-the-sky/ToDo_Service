from rest_framework.viewsets import ModelViewSet

from rest_framework.pagination import LimitOffsetPagination
from profiles.models import Project, ToDo
from profiles.serializers import ProfileModelSerializer, ToDoModelSerializer
from profiles.filtres import ProjectFilter, ToDoFilter

class ProfileLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10

class ToDoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20

class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProfileModelSerializer
    pagination_class = ProfileLimitOffsetPagination
    filterset_class = ProjectFilter


class ToDoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer
    pagination_class = ToDoLimitOffsetPagination
    filterset_class = ToDoFilter
