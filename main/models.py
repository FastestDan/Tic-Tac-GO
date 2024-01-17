from django.db import models


class Lobby(models.Model):
    name = models.CharField(max_length=200)
    guest = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Move(models.Model):
    player = models.CharField(max_length=200)
    gridnum = models.IntegerField()
