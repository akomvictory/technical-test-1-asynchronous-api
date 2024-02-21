from rest_framework.response import Response
from rest_framework.decorators import api_view
import aiohttp
import asyncio
from django.http import HttpResponse
import requests

from api_async_app.serializers import QuoteSerializer


@api_view(['GET'])
def get_quotes(request):
   
    response = requests.get('https://quotable.io/quotes?page=1')
    try:
        quote_data = response.json()
        quote_serializer = QuoteSerializer(data=quote_data['results'], many=True)
        quote_serializer.is_valid()
    except Exception as es:
        print(es)    
    return Response(quote_serializer.data)

@api_view(['GET'])
def get_random_user(request):
   
    user_response = requests.get('https://randomuser.me/api/')
    try:
        user_data =  user_response.json()
    except Exception as es:
        print(es)    
    return Response(user_data)