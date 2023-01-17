from .serializers import PropertyModelSerializer, CarListPropertyModelsSerializer
from .models import Property
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class PropertyAPI(APIView):

    def get(self, request, format=None):
        queryset = Property.objects.all()
        serializer = PropertyModelSerializer(queryset, many=True)
        city_name = self.request.query_params.get('city_name', None)
        state_name = self.request.query_params.get('state_name', None)
        property_id = self.request.query_params.get('property_id', None)
        
        
        if city_name is not None:
            queryset = queryset.filter(city=city_name)
            serializer = PropertyModelSerializer(queryset, many=True)

        if property_id is not None:
            data = queryset.values_list('city', flat=True).get(id=property_id)
            print(str(data))
            queryset = queryset.filter(city=data)
            print(queryset)
            serializer = PropertyModelSerializer(queryset, many=True)

        if state_name is not None:
            queryset = queryset.filter(state=state_name)
            serializer = CarListPropertyModelsSerializer(queryset, many=True)

        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = PropertyModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):

        id = pk
        stu = Property.objects.get(pk=id)
        serializer = PropertyModelSerializer(stu, data=request.data) # all field must be update
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_206_PARTIAL_CONTENT)