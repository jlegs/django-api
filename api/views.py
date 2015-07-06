import json
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from api.models import FizzBuzz


@api_view(['GET',])
def fizzbuzz(request):
    '''
    Takes a GET request at /api with the parameters 'word' and 'max_value', and returns
    a json-formatted response containing the numbers correlating to the fizzbuzz test for the provided word and 
    max_value, plus a status code.
    '''

    # Set a 400 error first because we change this var fewer times if we do that
    stat = {'code': status.HTTP_400_BAD_REQUEST, 'message': 'error'}

    try:
        word = request.query_params['word']
        max_value = int(request.query_params['max_value'])
    except (MultiValueDictKeyError, ValueError):
        # MultiValueDictKeyError in case the keys we're looking for don't exist in .query_params
        # ValueError in case people use quotes, floats or other junk in the request parameters
        word = None
        max_value = None

    if word in ('fizz', 'buzz', 'fizzbuzz') and max_value > 0: # check for valid param vals here
        stat = {'code': status.HTTP_200_OK, 'message': 'ok'}

    fizzbuzz = FizzBuzz(max_value=max_value, word=word)
    fizzbuzz_dict = fizzbuzz.create_fizzbuzz_dict()
    fizzbuzz_dict['status'] = stat['message']

    return Response(fizzbuzz_dict, status=stat['code'])




