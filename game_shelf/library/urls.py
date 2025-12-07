from django.urls import path
from . import views

app_name = "library"

urlpatterns = [
    path("search/", views.search_view, name="search"),
    path("game/<int:rawg_id>/", views.detail_view, name="detail"),
    path("game/<int:rawg_id>/add/", views.add_to_library, name="add_to_library"),
    path("my-library/", views.my_library, name="my_library"),
    path("game/<int:rawg_id>/review/", views.add_review, name="add_review"),
    path('game/<int:rawg_id>/update_shelf/', views.update_shelf, name='update_shelf'),
]
