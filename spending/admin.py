from django.contrib import admin
from .models import Goal, SpendingHabit, Transaction

admin.site.register(Goal)
admin.site.register(SpendingHabit)
admin.site.register(Transaction)

# Register your models here.
