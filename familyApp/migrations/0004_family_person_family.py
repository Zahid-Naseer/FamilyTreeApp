from django.db import migrations, models
import django.db.models.deletion


def create_default_family(apps, schema_editor):
    Family = apps.get_model('familyApp', 'Family')
    User   = apps.get_model('auth', 'User')

    user = User.objects.first()
    if user is None:
        return

    family = Family.objects.create(
        id=1,
        name="Default Family",
        created_by=user,
        invite_code="AAAAAAAA"
    )
    family.members.add(user)


class Migration(migrations.Migration):

    dependencies = [
        ('familyApp', '0003_person_gender'),   # ← fixed
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('invite_code', models.CharField(max_length=20, unique=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owned_families', to='auth.user')),
                ('members', models.ManyToManyField(blank=True, related_name='families', to='auth.user')),
            ],
        ),

        migrations.RunPython(create_default_family, migrations.RunPython.noop),

        migrations.AddField(
            model_name='person',
            name='family',
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='persons',
                to='familyApp.family',
            ),
            preserve_default=False,
        ),
    ]