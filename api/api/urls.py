from django.urls import path
from . import views


urlpatterns = [
    path('accounts/', views.AccountListViewSet.as_view({'get': 'list'})),
    path('status/<uuid:pk>/', views.AccountDetailViewSet.as_view({'get': 'retrieve'})),
    path('add/<uuid:pk>/', views.AccountAddBalanceViewSet.as_view({'post': 'update'})),
    path('subtract/<uuid:pk>/', views.AccountSubtractBalanceViewSet.as_view({'post': 'update'})),
    path('ping/', views.ping)
]
