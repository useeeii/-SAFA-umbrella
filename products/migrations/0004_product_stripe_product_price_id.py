from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('products', '0003_auto_20220824_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stripe_product_price_id',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]