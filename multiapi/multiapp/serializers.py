from rest_framework import serializers
from .models import ImageProduct

class ProductImageSerializer(serializers.ModelSerializer):
    upload_images = serializers.ListField(
        child=serializers.ImageField(max_length=100000, allow_empty_file=False, use_url=False),
        write_only=True
    )
    
    class Meta:
        model = ImageProduct
        fields = ['id', 'image', 'upload_images']

    def create(self, validated_data):
        uploaded_images = validated_data.pop('upload_images', [])  
        
       
        image_products = []
        for image in uploaded_images:
            image_products.append(ImageProduct(image=image))
        
        
        ImageProduct.objects.bulk_create(image_products)
        
    
        return validated_data
