from rest_framework.views import APIView
from django.http import JsonResponse

from utils.utils import get_env
from utils.test_selenium import test
import os


apiBaseKey = get_env("apiBaseKey",'astrit123')
print(apiBaseKey)
class API(APIView):
    def post(self,request):
        apiKey = request.data['apiKey']
        if apiKey == apiBaseKey:
            test()
            return JsonResponse({'status':True,'msg':'Succesfully submited ticket'},status=200)
        return JsonResponse({'status':'False','msg':'Cannot submit ticket','data':{}},status=400)   