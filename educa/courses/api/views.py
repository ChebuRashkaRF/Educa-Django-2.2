from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from ..models import Subject, Course
from .serializers import SubjectSerializer, CourseSerializer, CourseWithContentsSerializer
from .permissions import IsEnrolled


class SubjectListView(generics.ListAPIView):
    """Список предметов"""

    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetailView(generics.RetrieveAPIView):
    """Конкретный предмет"""

    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


# class CourseEnrollView(APIView):
#     """Обработчик зачисляет студентов на курсы"""
#
#     authentication_classes = (BasicAuthentication,)
#     permission_classes = (IsAuthenticated,)
#
#     def post(self, request, pk, format=None):
#         corse = get_object_or_404(Course, pk=pk)
#         corse.students.add(request.user)
#         return Response({'enrolled': True})


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    """Обработчик только для чтения курсов"""

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=True, methods=['post'],
                           authentication_classes=[BasicAuthentication],
                           permission_classes=[IsAuthenticated])
    def enroll(self, request, *args, **kwargs):
        """Обработчик зачисляет студентов на курсы"""

        course = self.get_object()
        course.students.add(request.user)
        return Response({'enrolled': True})

    @action(detail=True,
            methods=['get'],
            serializer_class=CourseWithContentsSerializer,
            authentication_classes=[BasicAuthentication],
            permission_classes=[IsAuthenticated, IsEnrolled])
    def contents(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
