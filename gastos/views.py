from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Departamento, Gasto
import json
from datetime import datetime
from django.shortcuts import render


def home(request):
    return render(request, 'gastos/home.html')


# Vista para generar gastos
def generar_gastos_html(request):
    return render(request, 'gastos/generar_gastos.html')

# Vista para registrar pagos
def marcar_pagado_html(request):
    return render(request, 'gastos/marcar_pagado.html')

# Vista para consultar pendientes
def listar_pendientes_html(request):
    return render(request, 'gastos/listar_pendientes.html')




@csrf_exempt
def generar_gastos(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        mes = data.get('mes')
        año = data.get('año')
        monto = data.get('monto', 10000)

        departamentos = Departamento.objects.all()
        for depto in departamentos:
            Gasto.objects.create(
                departamento=depto,
                mes=mes,
                año=año,
                monto=monto
            )
        return JsonResponse({"mensaje": "Gastos generados correctamente"}, status=200)

@csrf_exempt
def marcar_pagado(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        departamento_num = data.get('departamento')
        mes = data.get('mes')
        año = data.get('año')
        fecha_pago = data.get('fecha_pago')

        try:
            departamento = Departamento.objects.filter(numero=str(departamento_num)).first()
            gasto = Gasto.objects.get(departamento=departamento, mes=mes, año=año)

            if gasto.pagado:
                return JsonResponse({"estado": "Pago duplicado"}, status=400)
            gasto.pagado = True
            gasto.fecha_pago = datetime.strptime(fecha_pago, '%Y-%m-%d')
            gasto.save()
            return JsonResponse({"estado": "Pago registrado correctamente"}, status=200)
        except Departamento.DoesNotExist:
            return JsonResponse({"error": "Departamento no encontrado"}, status=404)
        except Gasto.DoesNotExist:
            return JsonResponse({"error": "Gasto no encontrado"}, status=404)

@csrf_exempt
def listar_pendientes(request):
    if request.method == 'GET':
        mes = int(request.GET.get('mes'))
        año = int(request.GET.get('año'))

        pendientes = Gasto.objects.filter(pagado=False, año__lt=año) | Gasto.objects.filter(
            pagado=False, año=año, mes__lte=mes
        )

        resultado = [
            {"departamento": gasto.departamento.numero, "periodo": f"{gasto.mes}/{gasto.año}", "monto": float(gasto.monto)}
            for gasto in pendientes
        ]
        return JsonResponse(resultado, safe=False, status=200)
