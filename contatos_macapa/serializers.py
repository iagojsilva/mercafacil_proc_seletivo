from rest_framework import serializers

from .models import ContatoMacapa

class ContatoMacapaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContatoMacapa
        fields = '__all__'


class CreateListModelMixin():
    def get_serializer(self, *args, **kwargs):
        """se for uma lista seta many to true"""
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super(CreateListModelMixin, self).get_serializer(*args, **kwargs)