from rest_framework.response import Response
from rest_framework.decorators import api_view
import aiohttp
import asyncio
from django.http import HttpResponse


from api_async_app.serializers import QuoteSerializer


async def fetch_quote():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://quotable.io/quotes?page=1') as response:
            return await response.json()

async def fetch_random_user():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://randomuser.me/api/') as response:
            return await response.json()

@api_view(['GET'])
async def get_quotes(request):
    quote_data = await fetch_quote()
    quote_serializer = QuoteSerializer(data=quote_data['results'], many=True)
    quote_serializer.is_valid()
    return HttpResponse(quote_serializer.data)

@api_view(['GET'])
async def get_random_user(request):
    user_data = await fetch_random_user()
    return HttpResponse(user_data)