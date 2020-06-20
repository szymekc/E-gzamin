from rest_framework import serializers
from E_gzamin_app.models import *
from django.contrib.auth.models import User


class BaseEntitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BaseEntity
        fields = ['url', 'id', 'createdAt', 'removedAt']


class AnswerSerializer(BaseEntitySerializer):
    class Meta:
        model = Answer
        fields = BaseEntitySerializer.Meta.fields + ['content', 'isCorrect', 'question']

    def create(self, validated_data):
        answer = Answer.objects.create(**validated_data)
        return answer

    def update(self, instance, validated_data):
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance


class CourseSerializer(BaseEntitySerializer):
    class Meta:
        model = Course
        fields = BaseEntitySerializer.Meta.fields + ['name']

    def create(self, validated_data):
        course = Course.objects.create(**validated_data)
        return course

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class DesignateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Designate
        group_id = serializers.CharField(source="group.id", read_only=True)
        testTemplate_id = serializers.CharField(source="testTemplate.id", read_only=True)
        fields = ['time', 'startDate', 'endDate', 'passReq' , 'id', 'group_id', 'testTemplate_id']

class GroupSerializer(BaseEntitySerializer):
    class Meta:
        model = Group
        fields = BaseEntitySerializer.Meta.fields + ['name', 'groupCode', 'openedAt', 'closedAt', 'members']

    def create(self, validated_data):
        group = Group.objects.create(**validated_data)
        return group


class QuestionSerializer(BaseEntitySerializer):
    class Meta:
        model = Question
        fields = BaseEntitySerializer.Meta.fields + ['content']

    def create(self, validated_data):
        user = self.context['request'].user
        question = Question.objects.create(owner=user, **validated_data)
        return question

    def update(self, instance, validated_data):
        instance.content = validated_data.get('content', instance.content)
        return instance


class TestResultSerializer(BaseEntitySerializer):
    class Meta:
        model = TestResult
        fields = BaseEntitySerializer.Meta.fields + ['result', 'maxPoints', 'isPassed',
                                                     'completedAt', 'startedAt', 'finishedAt','user_id']


class TestTemplateSerializer(BaseEntitySerializer):
    class Meta:
        model = TestTemplate
        fields = BaseEntitySerializer.Meta.fields + ['name','questions']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'is_member_of']
