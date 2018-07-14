from adaptor import adaptor
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

class AdaptorDnfView(APIView):
    def post(self, request, *args, **kwargs):
        resp = {}
        if (not "format" in request.data or not "policy" in request.data or not "tenant" in request.data or not "apf" in request.data):
            resp['detail'] = "Missing argument"
            return Response(resp, status=412)
        elif (request.data["format"] == "gcloud"):
            resp = adaptor.policy2dnf(request.data["policy"], request.data["tenant"], request.data["apf"])
            return Response(resp)
        else:
            resp['detail'] = "Policy Format not Supported."
            return Response(resp, status=415)

class AdaptorLocalView(APIView):
    def post(self, request, *args, **kwargs):
        return Response(adaptor.policy2local(request.data))
