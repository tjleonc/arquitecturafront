from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    # Vistas HTML
    path('generar_gastos/', views.generar_gastos_html, name='generar_gastos_html'),
    path('marcar_pagado/', views.marcar_pagado_html, name='marcar_pagado_html'),
    path('listar_pendientes/', views.listar_pendientes_html, name='listar_pendientes_html'),
    
    # Endpoints de la API
    path('api/generar_gastos/', views.generar_gastos, name='generar_gastos'),
    path('api/marcar_pagado/', views.marcar_pagado, name='marcar_pagado'),
    path('api/listar_pendientes/', views.listar_pendientes, name='listar_pendientes'),
]
