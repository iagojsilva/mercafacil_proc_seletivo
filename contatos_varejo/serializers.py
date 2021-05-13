from rest_framework import serializers
from .validate import celular_valido
from .models import ContatoVarejo

class ContatoVarejoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContatoVarejo
        fields = '__all__'

    def validate_celular(self, num_celular):
        if not celular_valido(num_celular):
            raise serializers.ValidationError('O celular deve esta no seguinte padrao: 554130306905')
        return num_celular

class CreateListModelMixin():
    def get_serializer(self, *args, **kwargs):
        """se for uma lista seta many to true"""
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super(CreateListModelMixin, self).get_serializer(*args, **kwargs)