from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm
# Create your views here.
ctx = {}
def index(request):
    if request.method == 'POST' and 'firstSentence' in request.POST:
        ctx['firstSentence'] = str(request.POST.get('firstSentence',''))
        ctx['secondSentence'] = str(request.POST.get('secondSentence',''))
        print(ctx)
    return render(request, 'DecWeb/index.html', ctx)

import pickle
loaded_model = pickle.load(open('trained_model\xgb_model.pickle.dat', 'rb'))





# def postForm(request):
#     a = PostForm()
#     return render(request, 'DecWeb/index.html',{'f': a})
# def save(request):
#     if request.method == "POST":
#         f = postForm(request.POST)
#         if f.is_valid():
#             f.save()
#             return HttpResponse("Da luu")
#         else:
#             return("Chua luu")
#     return('Sai roi')