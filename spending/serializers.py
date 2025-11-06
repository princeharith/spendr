from rest_framework import serializers
from .models import Goal, SpendingHabit, Transaction

class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = '__all__'

class SpendingHabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpendingHabit
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'