from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import WisataForm
from .models import Wisata


def index(request):
    status = ''
    if request.method == 'POST':
        form = WisataForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = WisataForm()
        return render(request, 'pariwisata/index.html', {'form': form, 'Wisatas': Wisata.objects.all(), 'status': status })

def edit(request, pk):
    wisata = get_object_or_404(Wisata, pk=pk)
    status = 'success'
    nama_wisataValue = Wisata.objects.filter(pk=pk).values('nama_wisata')[0];
    Wisata_nama_wisata = nama_wisataValue['nama_wisata']
    
    if request.method == 'POST':
        post_form = WisataForm(request.POST, instance=Wisata)
        if post_form.is_valid():
            post_form.save()
            return render(request, 'pariwisata/edit.html', {'form': post_form, 'status': status, 'nama_wisata': Wisata_nama_wisata })
    else:
        form = WisataForm(instance=Wisata)
        return render(request, 'pariwisata/edit.html', {'form': form, 'Wisata_nama_wisata': Wisata_nama_wisata })

def delete(request, pk):
    wisata = Wisata.objects.get(pk=pk)
    Wisata.delete()
    return HttpResponseRedirect('/')
