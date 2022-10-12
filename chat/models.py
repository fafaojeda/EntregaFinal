from django.contrib.auth.models import User
from django.db import models


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    message = models.CharField(max_length=1200)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.message , self.sender
    class Meta:
        ordering = ('timestamp',)

# ------------------------------------------------------------------------------------------------

class blog(models.Model):
    titulo      = models.CharField(max_length=80)
    subtitulo   = models.CharField(max_length=80)
    cuerpo      = models.CharField(max_length=5000)
    autor       = models.CharField(max_length=50)
    fecha       = models.DateField ()
    imagen      = models.ImageField(upload_to='media', null=True, blank=True)

    def __str__(self):
        return self.titulo , self.autor , self.fecha, self.imagen
