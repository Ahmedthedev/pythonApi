from rest_framework import serializers

from .models import Professor, Student, Classe, Subject, Promotion


class ProfessorSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Professor
        fields = ('id','firstname','lastname','fk')

class StudentSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Student
        fields = ('id','firstname','lastname')


class PromotionSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Promotion
        fields = ('id','code','name')


class ClasseSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Classe
        fields = ('id','firstname','lastname')


class SubjectSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Subject
        fields = ('id','firstname','lastname')
