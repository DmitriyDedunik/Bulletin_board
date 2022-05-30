# Generated by Django 4.0.4 on 2022-05-30 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin_board_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Группа')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группа',
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-create'], 'verbose_name': 'Публикация', 'verbose_name_plural': 'Публикация'},
        ),
        migrations.AddField(
            model_name='post',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bulletin_board_app.group', verbose_name='Группа'),
        ),
    ]