from django.db import models


class Package(models.Model):
    title = models.CharField(max_length=30)


class Itinerary(models.Model):
    package = models.ForeignKey(
        Package, on_delete=models.CASCADE, related_name="itinerary"
    )
    title = models.CharField(max_length=30)


class Activity(models.Model):
    itinerary = models.ForeignKey(
        Itinerary, on_delete=models.CASCADE, related_name="activity"
    )
    title = models.CharField(max_length=30)
