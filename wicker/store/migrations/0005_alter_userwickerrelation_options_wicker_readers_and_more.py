# Generated by Django 4.0.4 on 2022-05-14 16:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0004_userwickerrelation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userwickerrelation',
            options={'verbose_name': 'Отношение Юзер Корзинка', 'verbose_name_plural': 'Отношение Юзеры Корзинки'},
        ),
        migrations.AddField(
            model_name='wicker',
            name='readers',
            field=models.ManyToManyField(related_name='wickers', through='store.UserWickerRelation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='wicker',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='my_wickers', to=settings.AUTH_USER_MODEL),
        ),
    ]