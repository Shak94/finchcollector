from django.db import models

class Shark(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    bio = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class SharkInfo(models.Model):
    species = models.CharField(max_length=100)
    discovered = models.IntegerField(default=0000)
    shark = models.ForeignKey(Shark, on_delete=models.CASCADE, related_name='more')
    
    class Meta:
        ordering = ['species']
