from django.db import models

class Yonalish(models.Model):
    nom = models.CharField(max_length=255)
    aktiv = models.BooleanField(default=True)

    def __str__(self):
        return self.nom
    class Meta:
        verbose_name_plural='Yonalishlar'



class Fan(models.Model):
    nom = models.CharField(max_length=255)
    yonalish = models.ForeignKey(Yonalish, on_delete=models.SET_NULL,null=True)
    asosiy = models.BooleanField(default=False)

    def __str__(self):
        return self.nom
    class Meta:
        verbose_name_plural='Fanlar'

class Ustoz(models.Model):
    ISHOV = [
        ('Bakalavr', 'Bakalavr'),
        ('Magistr', 'Magistr'),
        ('Doktorant', 'Doktorant'),
        ('Professor', 'Professor'),

    ]

    ism = models.CharField(max_length=255)
    jins = models.CharField(max_length=10)
    yosh = models.PositiveIntegerField()
    daraja = models.CharField(max_length=50, choices=ISHOV)
    fan = models.ForeignKey(Fan, on_delete=models.SET_NULL,null=True)
    class Meta:
        verbose_name_plural='Ustozlar'
    def __str__(self):
        return self.ism
