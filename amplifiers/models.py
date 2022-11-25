from django.db import models


# Create your models here.

class Amplifier(models.Model):
    amplifier_type_choice = (
        (0, 'Pre-Amp'),
        (1, 'Power-Amp')
    )
    model = models.CharField('Amplifier Model', max_length=128, unique=True)
    amplifier_type = models.SmallIntegerField('Amplifier Type', choices=amplifier_type_choice, default=0)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE, verbose_name="Amplifier Manufacturer")
    description = models.TextField()
    specification = models.TextField()
    picture = models.BinaryField(null=True, blank=True, editable=True)
    content_type = models.CharField(max_length=256, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = "Amplifier"
        verbose_name_plural = "Amplifier"


class Manufacturer(models.Model):
    name = models.CharField('Amplifier Manufacturer Name', max_length=128)
    text = models.TextField('Manufacturer Description')
    existed = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Manufacturer"
        verbose_name_plural = "Manufacturer"