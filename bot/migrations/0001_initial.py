# Generated by Django 4.1.3 on 2022-11-24 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Berry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='Ягода')),
                ('price', models.DecimalField(decimal_places=2, max_digits=19, verbose_name='Цена')),
            ],
        ),
        migrations.CreateModel(
            name='Cake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, verbose_name='название торта')),
                ('description', models.TextField(blank=True, verbose_name='описание торта')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='', verbose_name='изображение торта')),
                ('default', models.BooleanField(default=False, verbose_name='торт в ассортименте')),
                ('berries', models.ManyToManyField(related_name='cakes', to='bot.berry', verbose_name='ягоды')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=200, verbose_name='клиент')),
                ('phone', models.CharField(max_length=12, verbose_name='клиент')),
                ('address', models.TextField(help_text='ул. Подольских курсантов д.5 кв.4', verbose_name='Адрес квартиры')),
            ],
        ),
        migrations.CreateModel(
            name='Layer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Количество слоев')),
                ('price', models.DecimalField(decimal_places=2, max_digits=19, verbose_name='Цена')),
            ],
        ),
        migrations.CreateModel(
            name='Shape',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shape', models.CharField(max_length=32, verbose_name='Форма коржа')),
                ('price', models.DecimalField(decimal_places=2, max_digits=19, verbose_name='Цена')),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='Топпинг')),
                ('price', models.DecimalField(decimal_places=2, max_digits=19, verbose_name='Цена')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, verbose_name='комментарий к заказу')),
                ('order_price', models.DecimalField(decimal_places=2, max_digits=19, verbose_name='Сумма заказа')),
                ('order_time', models.DateTimeField(auto_now_add=True, verbose_name='время создания')),
                ('cakes', models.ManyToManyField(related_name='orders', to='bot.cake', verbose_name='торты')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='bot.client', verbose_name='клиент')),
            ],
        ),
        migrations.AddField(
            model_name='cake',
            name='layers',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cakes', to='bot.layer', verbose_name='слои'),
        ),
        migrations.AddField(
            model_name='cake',
            name='shape',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cakes', to='bot.shape', verbose_name='форма'),
        ),
        migrations.AddField(
            model_name='cake',
            name='toppings',
            field=models.ManyToManyField(related_name='cakes', to='bot.topping', verbose_name='топинги'),
        ),
    ]