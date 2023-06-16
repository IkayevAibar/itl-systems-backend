from rest_framework import serializers
from .models import Lead, TextContent, ImageContent

class LeadSerializer(serializers.ModelSerializer):
    def validate_phone(self, phone):
        cleaned_phone = ''.join(filter(str.isdigit, phone))
        if len(cleaned_phone) not in [11, 12]:
            raise serializers.ValidationError("Некорректный номер телефона")
        return cleaned_phone
    
    def validate_name(self, name):
        if len(name) < 2:
            raise serializers.ValidationError("Имя должно содержать не менее двух символов")
        return name
    
    def validate(self, attrs):
        attrs = super().validate(attrs)
        # Дополнительная валидация или проверка других полей
        return attrs
    
    class Meta:
        model = Lead
        fields = '__all__'

class TextContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextContent
        fields = '__all__'

class ImageContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageContent
        fields = '__all__'