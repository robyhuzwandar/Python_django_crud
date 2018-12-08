from django.db import models

# Create your models here.
class Wisata(models.Model):
    jenis_wisatawan_choice = (
        ('Religi', 'Religi'),
        ('Alam', 'Alam'),
        ('Tradisional', 'Tradisional'),
        ('Buatan', 'Buatan'),
    )
    nama_wisata = models.CharField(max_length=50)
    jenis_wisata = models.CharField(max_length=25, choices=jenis_wisatawan_choice, default='Alam')
    biaya_masuk = models.CharField(max_length=50)
    min_harga_makanan = models.CharField(max_length=50)
    biaya_transport = models.CharField(max_length=50)
    min_harga_penginapan = models.CharField(max_length=50)
    jarak_dari_bandara = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nama_wisata
    
