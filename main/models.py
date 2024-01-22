from django.db import models


class Lobby(models.Model):
    name = models.CharField(max_length=200)
    guest = models.CharField(max_length=200)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Move(models.Model):
    player = models.CharField(max_length=200)
    gridnum = models.IntegerField()
    objects = models.Manager()


class Player(models.Model):
    name = models.CharField(max_length=100)
    # Другие поля, связанные с игроком


class Game(models.Model):
    room = models.ForeignKey(Lobby, on_delete=models.CASCADE)
    # Другие поля, связанные с состоянием игры
