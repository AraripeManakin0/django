from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json

@csrf_exempt
def make_move(request):
    state = json.loads(request.body)
    difficulty = state['difficulty']
    if difficulty == "easy":
        move = minimax()
    elif difficulty == "medium":
        move = alphabeta()
    else:
        move = alphabeta()
    return JsonResponse(move)


def minimax():
    return { 'color': 'black' }


def alphabeta():
    return { 'color': 'black' }
