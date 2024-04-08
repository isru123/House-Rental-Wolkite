from django.db import migrations


def set_default_created_by(apps, schema_editor):
    ConversationMessage = apps.get_model('message', 'ConversationMessage')
    User = apps.get_model('auth', 'User')
    default_user = User.objects.first()  # Change this to select the appropriate default user

    ConversationMessage.objects.filter(created_by=None).update(created_by=default_user)


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0008_conversationmessage_created_by'),
    ]

    operations = [
        migrations.RunPython(set_default_created_by),
    ]