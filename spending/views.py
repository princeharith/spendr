from django.shortcuts import render
from rest_framework import viewsets
from .models import Goal, SpendingHabit, Transaction
from .serializers import GoalSerializer, SpendingHabitSerializer, TransactionSerializer

class GoalViewSet(viewsets.ModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer

class SpendingHabitViewSet(viewsets.ModelViewSet):
    queryset = SpendingHabit.objects.all()
    serializer_class = SpendingHabitSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class =  TransactionSerializer
