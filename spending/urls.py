from rest_framework import routers
from .views import GoalViewSet, SpendingHabitViewSet, TransactionViewSet

router = routers.DefaultRouter()
router.register(r'goals', GoalViewSet)
router.register(r'spending_habits', SpendingHabitViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = router.urls

