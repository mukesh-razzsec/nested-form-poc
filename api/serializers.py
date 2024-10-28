from rest_framework import serializers

from api.models import Activity, Itinerary, Package


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ["title"]


class ItinerarySerializer(serializers.ModelSerializer):
    activity = ActivitySerializer(many=True)

    class Meta:
        model = Itinerary
        fields = ["title", "activity"]


class PackageSerializer(serializers.ModelSerializer):
    itinerary = ItinerarySerializer(many=True)

    class Meta:
        model = Package
        fields = ["title", "itinerary"]
