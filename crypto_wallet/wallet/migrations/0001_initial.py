
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(choices=[('ETH', 'ETHEREUM')], max_length=3)),
                ('address', models.CharField(max_length=42, unique=True)),
                ('private_key', models.CharField(max_length=255)),
            ],
        ),
    ]
