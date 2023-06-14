from django.db import models

# Create your models here.
class kelompok (models.Model):
    nama = models.CharField(max_length=12)
    keterangan=models.TextField()

    def __str__(self):
        return self.judul
    