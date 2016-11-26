from django.db import models
from django.forms import ModelForm
from django.contrib.postgres.fields import ArrayField


class Input(models.Model):

    R = models.FloatField(verbose_name=' resistencia (ohm)', default=1.0)
    L = models.FloatField(verbose_name=' inductancia (H)', default=0.5)
    Km = models.FloatField(verbose_name=' ctte fuerza electromotriz = ctte torque', default=0.01)
    b = models.FloatField(verbose_name=' coeficiente de friccion (Nms)', default=0.1)
    J = models.FloatField(verbose_name=' inercia (Kgm^2)', default=0.01)
    P = ArrayField(models.FloatField(), verbose_name=' Polos', default=[-1, -2, -3])


class InputForm(ModelForm):
    class Meta:
        model = Input
        fields = '__all__'
