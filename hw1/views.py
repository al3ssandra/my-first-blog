from django.shortcuts import render
from django.http import HttpResponse
from models import InputForm
from compute import compute
import os


def index(request):

    os.chdir(os.path.dirname(__file__))
    result = None
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form2 = form.save(commit=False)
            result = compute(form2.R, form2.L, form2.Km, form2.b, form2.J, form2.P)
            result = result.replace('static/', '')

    else:
        form = InputForm()

    return render(request, 'hw1.html', {'form': form, 'result': result, })