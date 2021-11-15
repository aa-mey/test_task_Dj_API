from rest_framework import serializers
from .models import Worker
from rest_framework_recursive.fields import RecursiveField

class WorkerSerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True)

    class Meta:
        model = Worker
        fields = (
            'name',
            'position',
            'date_start',
            'salary',
            'sum_salaries',
            'children',
        )

class WorkerSerializerOneLevel(serializers.ModelSerializer):

    class Meta:
        model = Worker
        fields = (
            'name',
            'position',
            'date_start',
            'salary',
            'sum_salaries',
        )