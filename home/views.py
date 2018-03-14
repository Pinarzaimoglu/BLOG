from django.shortcuts import render, HttpResponse


def home_view(request):
    if request.user.is_authenticated():
         context = {
	     'isim': 'Pinar',
          }
    else:
        context = {
	     'isim': 'Misafir Kullanici',
           } 
    return render(request,'home.html',context)


