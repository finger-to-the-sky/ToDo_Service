from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from profiles.models import Project, ToDo
from profiles.serializers import ProjectModelSerializer, ToDoModelSerializer
from profiles.filtres import ProjectFilter, ToDoFilter

class ProfileLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10

class ToDoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20

class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProfileLimitOffsetPagination
    filterset_class = ProjectFilter


class ToDoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer
    pagination_class = ToDoLimitOffsetPagination
    filterset_class = ToDoFilter

    def destroy(self, request, pk=None, **kwargs):
        todo = get_object_or_404(ToDo, pk=pk)
        todo.is_active = False
        todo.save()
        return Response(ToDoModelSerializer(todo, context={'request': request}).data)