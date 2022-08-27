from rest_framework.serializers import ModelSerializer, StringRelatedField

from users.models import User
from users.serializers import UserModelSerializer, HyperlinkedModelSerializer
from profiles.models import Project, ToDo


class UserListModelSerializer(UserModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class ToDoListSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ToDo
        fields = ('name', 'url', 'text', 'update_at', 'is_active')


class ProjectModelSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'url', 'repo_url', 'created_at', 'users',)


class ToDoModelSerializer(HyperlinkedModelSerializer):
    user = StringRelatedField()
    project = StringRelatedField()

    class Meta:
        model = ToDo
        fields = '__all__'