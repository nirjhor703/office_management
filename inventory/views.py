from .models.item_categories import ItemCategory
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import viewsets

# Create your views here.
# item category
class ItemCategoryCrud(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            #complex Data
            data = ItemCategory.objects.get(id=id)
            #python dict
            serializer = ItemCategorySerializer(data)

            return Response(serializer.data)
        
        #complex Data
        data = ItemCategory.objects.all()
        #python dict
        serializer = ItemCategorySerializer(data, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        # breakpoint()
        serialiser = ItemCategorySerializer(data=request.data)
        if serialiser.is_valid():
            serialiser.save()
            
            return Response({
                'msg':'Successfully inserted'
            })
        return Response(serialiser.errors)
    


    def put(self, request, pk, format=None):
        id = pk
        data = ItemCategory.objects.get(id=id)
        serialiser = ItemCategorySerializer(data, data=request.data)
        if serialiser.is_valid():
            serialiser.save()
            return Response({
                'msg':'Successfully Updated'
            })
        return Response(serialiser.errors)


    def patch(self, request, pk, format=None):
        id = pk
        data = ItemCategory.objects.get(id=id)
        serialiser = ItemCategorySerializer(data, data=request.data, partial=True)
        if serialiser.is_valid():
            serialiser.save()
            return Response({
                'msg':'Successfully Update Partial'
            })
        return Response(serialiser.errors)
    
    def delete(self, request, pk, format=None):
        id = pk
        data = ItemCategory.objects.get(id=id)
        data.delete()
        return Response({
            'msg':'Successfully Deleted'
        })
    
# item forms
class ItemFormCrud(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            #complex Data
            data = ItemForm.objects.get(id=id)
            #python dict
            serializer = ItemFormSerializer(data)

            return Response(serializer.data)
        
        #complex Data
        data = ItemForm.objects.all()
        #python dict
        serializer = ItemFormSerializer(data, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        # breakpoint()
        serialiser = ItemFormSerializer(data=request.data)
        if serialiser.is_valid():
            serialiser.save()
            
            return Response({
                'msg':'Successfully inserted'
            })
        return Response(serialiser.errors)
    


    def put(self, request, pk, format=None):
        id = pk
        data = ItemForm.objects.get(id=id)
        serialiser = ItemFormSerializer(data, data=request.data)
        if serialiser.is_valid():
            serialiser.save()
            return Response({
                'msg':'Successfully Updated'
            })
        return Response(serialiser.errors)


    def patch(self, request, pk, format=None):
        id = pk
        data = ItemForm.objects.get(id=id)
        serialiser = ItemFormSerializer(data, data=request.data, partial=True)
        if serialiser.is_valid():
            serialiser.save()
            return Response({
                'msg':'Successfully Update Partial'
            })
        return Response(serialiser.errors)
    
    def delete(self, request, pk, format=None):
        id = pk
        data = ItemForm.objects.get(id=id)
        data.delete()
        return Response({
            'msg':'Successfully Deleted'
        })
        
# item unit
class ItemUnitCrud(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            #complex Data
            data = ItemUnit.objects.get(id=id)
            #python dict
            serializer = ItemUnitSerializer(data)

            return Response(serializer.data)
        
        #complex Data
        data = ItemUnit.objects.all()
        #python dict
        serializer = ItemUnitSerializer(data, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        # breakpoint()
        serialiser = ItemUnitSerializer(data=request.data)
        if serialiser.is_valid():
            serialiser.save()
            
            return Response({
                'msg':'Successfully inserted'
            })
        return Response(serialiser.errors)
    


    def put(self, request, pk, format=None):
        id = pk
        data = ItemUnit.objects.get(id=id)
        serialiser = ItemUnitSerializer(data, data=request.data)
        if serialiser.is_valid():
            serialiser.save()
            return Response({
                'msg':'Successfully Updated'
            })
        return Response(serialiser.errors)


    def patch(self, request, pk, format=None):
        id = pk
        data = ItemUnit.objects.get(id=id)
        serialiser = ItemUnitSerializer(data, data=request.data, partial=True)
        if serialiser.is_valid():
            serialiser.save()
            return Response({
                'msg':'Successfully Update Partial'
            })
        return Response(serialiser.errors)
    
    def delete(self, request, pk, format=None):
        id = pk
        data = ItemUnit.objects.get(id=id)
        data.delete()
        return Response({
            'msg':'Successfully Deleted'
        })
# item manufacturer
class ItemManufacturerCrud(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            #complex Data
            data = ItemManufacturer.objects.get(id=id)
            #python dict
            serializer = ItemManufacturerSerializer(data)

            return Response(serializer.data)
        
        #complex Data
        data = ItemManufacturer.objects.all()
        #python dict
        serializer = ItemManufacturerSerializer(data, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        # breakpoint()
        serialiser = ItemManufacturerSerializer(data=request.data)
        if serialiser.is_valid():
            serialiser.save()
            
            return Response({
                'msg':'Successfully inserted'
            })
        return Response(serialiser.errors)
    


    def put(self, request, pk, format=None):
        id = pk
        data = ItemManufacturer.objects.get(id=id)
        serialiser = ItemManufacturerSerializer(data, data=request.data)
        if serialiser.is_valid():
            serialiser.save()
            return Response({
                'msg':'Successfully Updated'
            })
        return Response(serialiser.errors)


    def patch(self, request, pk, format=None):
        id = pk
        data = ItemManufacturer.objects.get(id=id)
        serialiser = ItemManufacturerSerializer(data, data=request.data, partial=True)
        if serialiser.is_valid():
            serialiser.save()
            return Response({
                'msg':'Successfully Update Partial'
            })
        return Response(serialiser.errors)
    
    def delete(self, request, pk, format=None):
        id = pk
        data = ItemManufacturer.objects.get(id=id)
        data.delete()
        return Response({
            'msg':'Successfully Deleted'
        })

# # ShowOne Update Delete Using ModelViewSet
# class StudentViewsetCrud(viewsets.ModelViewSet):
#     queryset = ItemCategory.objects.all()
#     serializer_class = ItemCategorySerializer

#     def list(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)
    
    
