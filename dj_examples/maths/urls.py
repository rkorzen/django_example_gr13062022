
from django.urls import path
from maths.views import hello_maths, handle_math, math_details

urlpatterns = [
    path("", hello_maths),       # localhost:8000/maths/
    path("<op>/<int:a>/<int:b>", handle_math, ),
    path("<m_id>/", math_details),
]
