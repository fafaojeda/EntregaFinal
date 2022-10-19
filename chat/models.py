from io import UnsupportedOperation
from django.contrib.auth.models import User
from django.db import models


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    message = models.CharField(max_length=1200)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.message
    class Meta:
        ordering = ('timestamp',)

class Blog(models.Model):
    titulo      = models.CharField(max_length=80)
    subtitulo   = models.CharField(max_length=80)
    cuerpo      = models.TextField(max_length=5000)
    autor       = models.CharField(max_length=10)
    fecha       = models.DateField()
    imagen      = models.ImageField(upload_to='media', null=True, blank=True)
    usuario     = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo +""+ self.subtitulo +""+ self.autor

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    imagen= models.ImageField(upload_to='avatares')
    def __str__(self):
        return self.imagen