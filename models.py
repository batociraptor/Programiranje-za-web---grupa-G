from django.db import models
from django.db.models.base import Model

# Create your models here.

class redatelj(models.Model):
    redatelj_ime = models.CharField(max_length=50)
    redatelj_prezime = models.CharField(max_length=50)
    redatelj_godina_rodenja = models.CharField(max_length=4)

    def __str__(self):
        return self.redatelj_prezime

class glumac(models.Model):
    glumac_ime = models.CharField(max_length=50)
    glumac_prezime = models.CharField(max_length=50)
    glumac_godina_rodenja = models.CharField(max_length=50)

    def __str__(self):
        return self.glumac_prezime


class studio(models.Model):
    studio_ime = models.CharField(max_length=50)
    studio_godina_osnivanja = models.CharField(max_length=4)

    def __str__(self):
        return self.studio_ime


class osoblje(models.Model):
    osoblje_ime = models.CharField(max_length=50)
    osoblje_prezime = models.CharField(max_length=50)
    osoblje_uloga = models.CharField(max_length=50)

    def __str__(self):
        return self.osoblje_ime



class reklama(models.Model):
    reklama_izdavac = models.CharField(max_length=50)
    reklama_trajanje = models.CharField(max_length=20)

    def __str__(self):
        return self.reklama_izdavac



class film(models.Model):
    film_ime = models.CharField(max_length=100)
    film_godina_objave = models.CharField(max_length=4)
    film_zanr = models.CharField(max_length=30)
    film_ocjena = models.CharField(max_length=20)
    film_budzet = models.CharField(max_length=10)
    film_drzava_proizvodnje = models.CharField(max_length=50)

    redatelj= models.ForeignKey(redatelj, default=1, on_delete=models.CASCADE,)
    glumac= models.ForeignKey(glumac, default=1, on_delete=models.CASCADE,)
    studio= models.ForeignKey(studio, default=1, on_delete=models.CASCADE,)
    osoblje= models.ForeignKey(osoblje, default=1, on_delete=models.CASCADE,)
    reklama= models.ForeignKey(reklama, default=1, on_delete=models.CASCADE,)


    def __str__(self):
        return self.film_ime

class serija(models.Model):
    serija_ime = models.CharField(max_length=100)
    serija_godina_objave = models.CharField(max_length=4)
    serija_zanr = models.CharField(max_length=30)
    serija_ocjena = models.CharField(max_length=20)
    serija_budzet = models.CharField(max_length=10)
    serija_drzava_proizvodnje = models.CharField(max_length=50)

    redatelj= models.ForeignKey(redatelj, default=1, on_delete=models.CASCADE,)
    glumac= models.ForeignKey(glumac, default=1, on_delete=models.CASCADE,)
    studio= models.ForeignKey(studio, default=1, on_delete=models.CASCADE,)
    osoblje= models.ForeignKey(osoblje, default=1, on_delete=models.CASCADE,)
    reklama= models.ForeignKey(reklama, default=1, on_delete=models.CASCADE,)


    def __str__(self):
        return self.serija_ime