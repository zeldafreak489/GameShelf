from django.shortcuts import render, redirect
from .utils import rawg_search, rawg_game_detail

def search_view(request):
    q = request.GET.get("q", "")
    results = []
    if q:
        data = rawg_search(q)
        results = data.get("results", [])
    return render(request, "library/search.html", {"query": q, "results": results})

def detail_view(request, rawg_id):
    game = rawg_game_detail(rawg_id)
    return render(request, "library/detail.html", {"game": game})
