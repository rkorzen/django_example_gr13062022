from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from maths.models import Math
from maths.services import MathService

def hello_maths(request):
    return HttpResponse("Witamy w świecie elementarnej matematki")

# /maths/add/1/2
# 3

def handle_math(request, op, a, b):
    result = MathService().handle(op, a, b)

    Math.objects.create(op=op, a=a, b=b, result=result)

    maths = Math.objects.all()

    context = {
        'maths': maths,
        'result': result
    }

    return render(
        request=request,
        template_name="maths/list.html",
        context=context
    )

# /maths/<m_id>
def math_details(request, m_id):
    # pobrac math od id = m_id
    math = Math.objects.get(pk=m_id)
    # wyrenderowac szabln przekazujac do niego pobrany math

    return render(
        request,
        "maths/details.html",
        {"math": math}
    )