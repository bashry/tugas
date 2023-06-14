from django.shortcuts import render

def daftar (request):
    judul=["jus jeruk", "jus aple", "jus leci",]
    pemilik="ach rofie bashry"

    konteks={
        'title':judul,
        'pemilik':pemilik,
    }
    return render(request,'daftar.html',konteks)

def tempat (request):
    return render(request,'tempat.html')

