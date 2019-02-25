# Generated by Django 2.1.7 on 2019-02-25 01:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0005_auto_20190224_1901'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConcreteBusiness',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField()),
                ('extras', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extras', models.TextField()),
                ('date_created', models.DateTimeField()),
                ('from_group', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='from_group', to='accounts.Group')),
                ('to_group', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='to_group', to='accounts.Group')),
            ],
        ),
        migrations.AddField(
            model_name='concretebusiness',
            name='reference',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='concrete_business', to='references.Reference'),
        ),
    ]
