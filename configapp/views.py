from rest_framework.templatetags.rest_framework import render_field
from rest_framework.views import APIView
from rest_framework.response import Response
import json

class Hello(APIView):
    def get(self, request):
        context ={
            "salom": "dunyo"
        }
        with open("data.json", 'r') as j:
            data = json.load(j)

        return Response(data=data)




    def post(self,request):
        name = request.data["name"]
        context ={
            "response":f"salom {name}"
        }
        return Response(data=context)


