from django.shortcuts import render
from .models import Car
from .serializers import CarSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView


#class CarListApiView(generics.ListAPIView):
#    queryset=Car.objects.all()
#    serializer_class = CarSerializer
class CarListApiView(APIView):
    def get(self, request):
        books=Car.objects.all()
        serializer=CarSerializer(books,many=True)
        return Response(serializer.data)

#class CarCreateApiView(generics.CreateAPIView):
#    queryset = Car.objects.all()
#    serializer_class = CarSerializer
class CarCreateApiView(APIView):
    def post(self,request):
        try:
            serializer=CarSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response({"status":"Nimadur xatto ketdi"})
        except:
            return Response({"status":"Nimadur xatto ketdi"})

#class CarEditApiView(generics.UpdateAPIView):
#    queryset = Car.objects.all()
#    serializer_class = CarSerializer
#    lookup_field = 'pk'
class CarEditApiView(APIView):
    def put(self,request,pk):
        cars=Car.objects.get(id=pk)
        serializer=CarSerializer(cars,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"xabar":"boldi yangilandi","yangilangani":serializer.data})
        else:
            return  Response({"javob":"Edit qilinmadi"})

    def patch(self,request,pk):
        cars=Car.objects.get(id=pk)
        serializer=CarSerializer(cars,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"xabar":"boldi yangilandi","yangilangani":serializer.data})
        else:
            return  Response({"javob":"Edit qilinmadi"})


#class CarDeleteApiView(generics.DestroyAPIView):
#    queryset = Car.objects.all()
#    serializer_class = CarSerializer
class CarDeleteApiView(APIView):
    def delete(self, request,pk):
        cars=Car.objects.get(id=pk)
        cars.delete()
        return Response({"xabar":"kitob ochirildi"})


#class CarDetailApView(generics.RetrieveAPIView):
#    queryset = Car.objects.all()
#    serializer_class = CarSerializer
class CarDetailApiView(APIView):
    def get(self,request,pk):
        try:
            cars=Car.objects.get(id=pk)
            serializer=CarSerializer(cars)
            return Response(serializer.data)
        except:
            return Response({"xabar":"bunday id-li kitob yuq mavjud emas"})


#class CarMixedApView(generics.RetrieveUpdateDestroyAPIView):
#    queryset = Car.objects.all()
#    serializer_class = CarSerializer
class CarMixedApiView(APIView):
    def get(self,request,pk):
        try:
            cars=Car.objects.get(id=pk)
            serializer=CarSerializer(cars)
            return Response(serializer.data)
        except:
            return Response({"xabar":"bunday id-li kitob yuq mavjud emas"})

    def put(self,request,pk):
        cars=Car.objects.get(id=pk)
        serializer=CarSerializer(cars,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"xabar":"boldi yangilandi","yangilangani":serializer.data})
        else:
            return  Response({"javob":"Edit qilinmadi"})

    def patch(self,request,pk):
        cars=Car.objects.get(id=pk)
        serializer=CarSerializer(cars,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"xabar":"boldi yangilandi","yangilangani":serializer.data})
        else:
            return  Response({"javob":"Edit qilinmadi"})


    def delete(self, request, pk):
        cars = Car.objects.get(id=pk)
        cars.delete()
        return Response({"xabar": "kitob ochirildi"})
