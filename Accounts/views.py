from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

    # Transaction Main Crud 
class TransactionMainCrud(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            #complex Data
            data = TransactionMain.objects.get(id=id)
            #python dict
            serializer = TransactionMainSerializer(data)

            return Response(serializer.data)
        
        #complex Data
        data = TransactionMain.objects.all()
        #python dict
        serializer = TransactionMainSerializer(data, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        # breakpoint()
        serialiser = TransactionMainSerializer(data=request.data)
        if serialiser.is_valid():
            serialiser.save()
            
            return Response({
                'msg':'Successfully inserted'
            })
        return Response(serialiser.errors)
    


    def put(self, request, pk, format=None):
        id = pk
        data = TransactionMain.objects.get(id=id)
        serialiser = TransactionMainSerializer(data, data=request.data)
        if serialiser.is_valid():
            serialiser.save()
            return Response({
                'msg':'Successfully Updated'
            })
        return Response(serialiser.errors)


    def patch(self, request, pk, format=None):
        id = pk
        data = TransactionMain.objects.get(id=id)
        serialiser = TransactionMainSerializer(data, data=request.data, partial=True)
        if serialiser.is_valid():
            serialiser.save()
            return Response({
                'msg':'Successfully Update Partial'
            })
        return Response(serialiser.errors)
    
    def delete(self, request, pk, format=None):
        id = pk
        data = TransactionMain.objects.get(id=id)
        data.delete()
        return Response({
            'msg':'Successfully Deleted'
        })
    

    # Transaction Head Crud 
class TransactionHeadCrud(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            #complex Data
            data = TransactionHead.objects.get(id=id)
            #python dict
            serializer = TransactionHeadSerializer(data)

            return Response(serializer.data)
        
        #complex Data
        data = TransactionHead.objects.all()
        #python dict
        serializer = TransactionHeadSerializer(data, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        # breakpoint()
        serialiser = TransactionHeadSerializer(data=request.data)
        if serialiser.is_valid():
            serialiser.save()
            
            return Response({
                'msg':'Successfully inserted'
            })
        return Response(serialiser.errors)
    


    def put(self, request, pk, format=None):
        id = pk
        data = TransactionHead.objects.get(id=id)
        serialiser = TransactionHeadSerializer(data, data=request.data)
        if serialiser.is_valid():
            serialiser.save()
            return Response({
                'msg':'Successfully Updated'
            })
        return Response(serialiser.errors)


    def patch(self, request, pk, format=None):
        id = pk
        data = TransactionHead.objects.get(id=id)
        serialiser = TransactionHeadSerializer(data, data=request.data, partial=True)
        if serialiser.is_valid():
            serialiser.save()
            return Response({
                'msg':'Successfully Update Partial'
            })
        return Response(serialiser.errors)
    
    def delete(self, request, pk, format=None):
        id = pk
        data = TransactionHead.objects.get(id=id)
        data.delete()
        return Response({
            'msg':'Successfully Deleted'
        })
    

    # Transaction Groupe Crud 
class TransactionGroupeCrud(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            #complex Data
            data = TransactionGroupe.objects.get(id=id)
            #python dict
            serializer = TransactionGroupeSerializer(data)

            return Response(serializer.data)
        
        #complex Data
        data = TransactionGroupe.objects.all()
        #python dict
        serializer = TransactionGroupeSerializer(data, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        # breakpoint()
        serialiser = TransactionGroupeSerializer(data=request.data)
        if serialiser.is_valid():
            serialiser.save()
            
            return Response({
                'msg':'Successfully inserted'
            })
        return Response(serialiser.errors)
    


    def put(self, request, pk, format=None):
        id = pk
        data = TransactionGroupe.objects.get(id=id)
        serialiser = TransactionGroupeSerializer(data, data=request.data)
        if serialiser.is_valid():
            serialiser.save()
            return Response({
                'msg':'Successfully Updated'
            })
        return Response(serialiser.errors)


    def patch(self, request, pk, format=None):
        id = pk
        data = TransactionGroupe.objects.get(id=id)
        serialiser = TransactionGroupeSerializer(data, data=request.data, partial=True)
        if serialiser.is_valid():
            serialiser.save()
            return Response({
                'msg':'Successfully Update Partial'
            })
        return Response(serialiser.errors)
    
    def delete(self, request, pk, format=None):
        id = pk
        data = TransactionGroupe.objects.get(id=id)
        data.delete()
        return Response({
            'msg':'Successfully Deleted'
        })