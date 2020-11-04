from django.shortcuts import render, redirect

def index(request):
    return render(request, "index.html")

def form(request):
    if request.method == 'GET':
        return redirect('/')
    if request.method == "POST":
        request.session['name'] = request.POST["name"]
        request.session['location'] = request.POST["location"]
        request.session['language'] = request.POST["language"]
        request.session['comment'] = request.POST["comment"]
    return redirect('/result')

def result(request):
    return render(request,'result.html')



