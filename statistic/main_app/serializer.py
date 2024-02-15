from rest_framework import serializers
from .models import Daily_Works


class Daily_work_api(serializers.ModelSerializer):
    class Meta:
        model = Daily_Works
        fields = "__all__"
