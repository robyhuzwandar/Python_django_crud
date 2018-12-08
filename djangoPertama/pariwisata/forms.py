from django.forms import ModelForm
from .models import Wisata

class WisataForm(ModelForm):

    class Meta:
        model = Wisata
        fields = ['nama_wisata', 'jenis_wisata', 'biaya_masuk', 'min_harga_makanan', 'biaya_transport', 'min_harga_penginapan','jarak_dari_bandara']