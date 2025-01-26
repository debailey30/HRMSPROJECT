from django.db import migrations
from django.db.migrations.operations.special import RunPython

class Migration(migrations.Migration):

    # The dependencies attribute specifies the migration files that this migration depends on.
    dependencies = [
        ('hrms_app', '0001_initial'),
    ]

    operations = [
        RunPython(RunPython.noop),
    ]