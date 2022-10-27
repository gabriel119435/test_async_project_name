from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dev',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('age', models.IntegerField()),
                ('level',
                 models.CharField(choices=[('junior', 'Jr'), ('middle', 'Md'), ('senior', 'Sn')], max_length=6)),
            ],
        ),
    ]
