from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import EnterpriseSerializer,CodeSerializer
from .models import Enterprise,Code
from django.http import Http404
from rest_framework import status
from django.db import models

# Create your views here.
#Endpoint1
class EnterPriseAPIView(APIView):
    serializer_class = CodeSerializer

    def get_queryset(self):
        enter = Enterprise.objects.all()
        return enter
    
    def get(self,request,*args,**kwargs):
        
        try:
            id_e = request.query_params["id"]
        
            print("el id es:\n\n\n\n\n\n\n\n ",id_e)
            enter = Code.objects.filter(owner=id_e)
            serializer = CodeSerializer(enter, many=True)
            
        except:
            enter = self.get_queryset()
            serializer = EnterpriseSerializer(enter, many=True)

        #serializer2 = CodeSerializer(code,many=True)
        
        return Response(serializer.data)

#Endpoint3
class NitEnterpriseAPIView(APIView):
    serializer_class = CodeSerializer
    def get_queryset(self):
        enter = Enterprise.objects.all()
        
        return enter
    def get(self,request,*args,**kwargs):
        serializer_Code = ''
        try:
            nit_e = request.query_params["nit"]
            #Sacamos del nit 
            enter = Enterprise.objects.get(nit=nit_e)
            serializer = EnterpriseSerializer(enter)
            #Extraemos el id de la empresa
            id_e = serializer.data["id"]
            

            #Buscamos ese id en codes
            code = Code.objects.filter(owner=id_e)
            print('Los codigos encontrados fueron ', code)
            serializer_Code = CodeSerializer(code,many=True)
            print(serializer.data,'el id es ',id_e,'esti es serializer \n\n',serializer_Code)

        except:
            enter = self.get_queryset()
            code = Code.objects.all()
            serializer = EnterpriseSerializer(enter,many=True)
            dic = serializer.data
                
            print('Esto es dic',dic)
            serializer2 = CodeSerializer(code,many=True)
            print(serializer.data)
        #Validamos que serializer_Code no sea vacio porque si lo es entonces solo debe de devolver el de todos 
        # SI no devuelve un diccionario
        if serializer_Code == '':
            res = serializer.data
        else:
            res = {
                "Enterprise":serializer.data,
                "codigos":serializer_Code.data
            }
        return Response(res)

#Endpoint4
class EnterpriseFromCodeAPIView(APIView):
    serializer_class = CodeSerializer

    def get_queryset(self):
        enter = Enterprise.objects.all()
        return enter
    
    def get(self,request,*args,**kwargs):
        
        try:
            #Tremos el id del codigo 
            id_e = request.query_params["id"]
            print("El id del codigo es \n\n\n",id_e)
            code = Code.objects.get(id=id_e)
            print("el codigo es \n\n\n",code)
            serializer = CodeSerializer(code)
            #Sacamos el id de enterprice
            id_enterprice = serializer.data["owner"]

            #Sacamos el id de la empresa
            enterprice = Enterprise.objects.get(id=id_enterprice)
            serializer_e = EnterpriseSerializer(enterprice)
            print("esto es \n\n serai",serializer_e.data)
            return Response(serializer_e.data)
        except:
            enter = self.get_queryset()
            serializer = EnterpriseSerializer(enter, many=True)
            return Response(serializer.data)
        #serializer2 = CodeSerializer(code,many=True)

