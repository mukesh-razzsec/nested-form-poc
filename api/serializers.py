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

    def create(self, validated_data):
        itinerary_data = validated_data.pop("itinerary")
        package = Package.objects.create(**validated_data)
        for item in itinerary_data:
            activity_data = item.pop("activity")
            itinerary = Itinerary.objects.create(package=package, **item)
            for active in activity_data:
                Activity.objects.create(itinerary=itinerary, **active)

        return package

    class Meta:
        model = Package
        fields = ["title", "itinerary"]
