import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .edModule import textCount, translateMyWord

# Create your views here.

class edTranslate(APIView):
    def get(self, request):
        #src_lang="eng_Latn", tgt_lang='hin_Deva'
        return Response('NLLB 200 Translator')
    def post(self, request):
        inputData = request.data['input']
        srcData = request.data['src']
        targetData = request.data['tgt']
        result = translateMyWord(inputData, srcData, targetData)
        return Response(result)