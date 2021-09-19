# Generated by Django 3.2.7 on 2021-09-10 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto', models.CharField(max_length=255)),
                ('preco_venda', models.DecimalField(decimal_places=2, max_digits=8)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estoque', models.CharField(max_length=255)),
                ('quantidade', models.IntegerField()),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='website.produto')),
            ],
        ),
    ]