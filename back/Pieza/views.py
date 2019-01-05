from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from Pieza.models import PiezaEje
from Pieza.serializers import PiezaSerializer
from Pieza.models import Ejecucion
from Pieza.serializers import EjecucionSerializer
from Pieza.models import ResultadoGeneral
from Pieza.serializers import ResultadoGeneralSerializer
from Pieza.models import PiezaResultado
from Pieza.serializers import PiezaResultadoSerializer
from algoritmos.Control import Control
import pdb
@csrf_exempt
def ejecucion_list(request):

    if request.method == 'GET':
        ejecucion= Ejecucion.objects.all()
        serializer = EjecucionSerializer(ejecucion, many=True)

        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        print(data)
        piezas_maquina = [[2, 3, 1], [2, 1, 2, 3], [3, 1, 2], [2, 3, 1, 2], [3, 2]]
        piezas_tiempo = [[2, 2, 1], [0.5, 2, 0.5, 2.5], [1.5, 2.5, 1], [1, 2.5, 3, 1], [0.5, 2]]
        control = Control(piezas_maquina, piezas_tiempo, data)
        control.algoritmo()
        serializer = EjecucionSerializer(data=data)

        if serializer.is_valid():
            #serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def pieza_list(request):

    if request.method == 'GET':
        piezas= PiezaEje.objects.all()
        serializer = PiezaSerializer(piezas, many=True)
        return JsonResponse(serializer.data, safe=False)
@csrf_exempt
def resultado_list(request):

    if request.method == 'GET':
        resultado= ResultadoGeneral.objects.all()
        serializer = ResultadoGeneralSerializer(resultado, many=True)
        return JsonResponse(serializer.data, safe=False)

def resultado_list_detail(request, pk):

    if request.method == 'GET':
        resultado= ResultadoGeneral.objects.get(pk=pk)
        serializer = ResultadoGeneralSerializer(resultado)
        return JsonResponse(serializer.data)
def pieza_resultado_list_detail(request, pk):

    if request.method == 'GET':
        resultado= PiezaResultado.objects.get(pk=pk)
        serializer = PiezaResultadoSerializer(resultado)
        return JsonResponse(serializer.data)