from django.urls import path
from . import views


urlpatterns = [
    path('accounts/', views.AccountListViewSet.as_view({'get': 'list'}), name='accounts'),
    path('status/<uuid:pk>/', views.AccountDetailViewSet.as_view({'get': 'retrieve'}), name='status'),
    path('add/<uuid:pk>/', views.AccountAddBalanceViewSet.as_view({'post': 'update'}), name='add'),
    path('subtract/<uuid:pk>/', views.AccountSubtractBalanceViewSet.as_view({'post': 'update'}), name='subtract'),
    path('ping/', views.ping)
]
