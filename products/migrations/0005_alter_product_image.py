from django.db import migrations, models

class Migrations(migrations.Migration):
    dependencies = [
        ('products', '0004_product_stripe_product_price_id'),
    ]

    operations= [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products_images'),
        ),
    ]