from django.urls import path
from Pieza import views

urlpatterns = [
    path('Pieza/', views.pieza_list),
    path('pieza/<int:pk>/', views.pieza_resultado_list_detail),
    path('ejecucion/', views.ejecucion_list),
    path('resultado/', views.resultado_list),
    path('resultado/<int:pk>/', views.resultado_list_detail)
]