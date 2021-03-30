from rest_framework import serializers
from content.models  import *
from rest_framework.permissions import IsAuthenticated

class ContentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'


class QuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class OpenQuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = OpenQuestion
        fields = '__all__'

class AlternativeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Alternative
        fields = '__all__'

class MultipleChoiceQuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = MultipleChoiceQuestion
        fields = '__all__'

class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class ActivityTeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model = ActivityTeacher
        fields = '__all__'

class ActivitySerializers(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'

class ActivityRealizationSerializers(serializers.ModelSerializer):
    class Meta:
        model = ActivityRealization
        fields = '__all__'

class ActivityRealizationTeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model = ActivityRealizationTeacher
        fields = '__all__'

class AnswerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'

class AnswerTeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'