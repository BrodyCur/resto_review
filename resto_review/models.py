from django.db import models

class Chef(models.Model):
  name = models.CharField(max_length=255)

class Restaurant(models.Model):
  name = models.CharField(max_length=255)
  location = models.CharField(max_length=255)
  chef = models.ManyToManyField(Chef)

class Publication(models.Model):
  title = models.CharField(max_length=255)

class Critic(models.Model):
  name = models.CharField(max_length=255)

class Review(models.Model):
  content = models.TextField()
  critic = models.ForeignKey(Critic, on_delete=models.CASCADE, related_name='reviews')
  publication = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name='reviews')
  restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='reviews')