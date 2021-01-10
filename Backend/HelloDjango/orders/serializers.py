from rest_framework import serializers

from .models import CallBack


class CallBackSerializer(serializers.ModelSerializer):
    """Заявки на обратный звонок"""

    class Meta:
        model = CallBack
        exclude = ('notice', 'date', 'update', 'complete')
