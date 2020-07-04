from rest_framework import serializers
from .models import *


class ActivityPeriodsSerializer(serializers.ModelSerializer):
    start_time = serializers.DateTimeField(format="%b %d %Y %I:%M%p")
    end_time = serializers.DateTimeField(format="%b %d %Y %I:%M%p")
    class Meta:
        model = ActivityPeriods
        fields = [
            'start_time',
            'end_time',
        ]


class MemberSerializer(serializers.ModelSerializer):
    activity_periods = ActivityPeriodsSerializer(many=True)
    class Meta:
        model = Member
        fields = [
            'id',
            'real_name',
            'tz',
            'activity_periods',
        ]
        depth = 1





