from django.contrib import admin
from django.urls import path
from api import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tarefas/all', views.get_tarefas),
    path('api/tarefas/<uuid:pk>', views.get_one_tarefa),
    path('api/tarefas/create', views.create_tarefa),
    path('api/tarefas/update/<uuid:pk>/', views.update_tarefa),
    path('api/tarefas/delete/<uuid:pk>/', views.delete_tarefa),
    path('api/user/create', views.create_user),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
