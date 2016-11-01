from django.shortcuts import render
from app.models import Batting, Fielding, Master, Pitching
from app.serializers import MasterSerializer, BattingSerializer, FieldingSerializer, PitchingSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# Create your views here.


class MasterListAPIView(ListCreateAPIView):
    queryset = Master.objects.all()
    serializer_class = MasterSerializer


class MasterDetailUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Master.objects.all()
    serializer_class = MasterSerializer


class BattingListAPIView(ListCreateAPIView):
    queryset = Batting.objects.all()
    serializer_class = BattingSerializer


class BattingDetailUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Batting.objects.all()
    serializer_class = BattingSerializer


class FieldingListAPIView(ListCreateAPIView):
    queryset = Fielding.objects.all()
    serializer_class = FieldingSerializer


class FieldingDetailUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Fielding.objects.all()
    serializer_class = FieldingSerializer


class PitchingListAPIView(ListCreateAPIView):
    queryset = Pitching.objects.all()
    serializer_class = PitchingSerializer


class PitchingDetailUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Pitching.objects.all()
    serializer_class = PitchingSerializer
