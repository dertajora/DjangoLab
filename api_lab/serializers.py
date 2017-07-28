class ProductSerializer (serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
        # fields = ['product_id']