from django.shortcuts import render

# Create your views here
def virat(request):
    d={'name':'rajiv','age':22}
    return render(request,'jinja.html',context=d)
