from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Mobiles
from rest_framework.viewsets import ViewSet
from api.serializer import MobileSerializer,MobileModelSerializer

class GadgetView(ViewSet):
    def list(self,requset,*args,**kwargs):
        qs=Mobiles.objects.all()
        serializer=MobileModelSerializer(qs,many=True)
        return Response(data=serializer.data)
    def create(self,request,*args,**kwargs):
        serializer=MobileModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Mobiles.objects.get(id=id)
        serializer=MobileModelSerializer(qs)
        return Response(data=serializer.data)
    def update(self,request,*args,**kwargs):
        id = kwargs.get("id")
        qs = Mobiles.objects.get(id=id)
        serializer=MobileModelSerializer(data=request.data,instance=qs)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:return Response(data=serializer.errors)
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Mobiles.objects.get(id=id).delete()
        return Response(data="deleted")



# Create your views here.
class MobilesView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Mobiles.objects.all()
        serializer=MobileModelSerializer(qs,many=True)
        return Response(data=serializer.data)
    def post(self,request,*args,**kw):
        serializer=MobileModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)



#localhost:8000/mobiles/1
class MobilesDetailView(APIView):
    def get(self,request,*args,**kw):
        id=kw.get("id")
        qs=Mobiles.objects.get(id=id)
        serializer=MobileModelSerializer(qs)
        return Response(data=serializer.data)

    def put(self,request,*args,**kw):
        id=kw.get("id")
        obj=Mobiles.objects.get(id=id)
        serializer=MobileModelSerializer(instance=obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return  Response(data=serializer.errors)

    def delete(self,request,*args,**kw):
        id=kw.get("id")
        qs=Mobiles.objects.get(id=id)
        qs.delete()
        return Response(data="delete")



