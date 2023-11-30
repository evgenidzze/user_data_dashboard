from django.db import models


class UserActions(models.Model):
    id = models.BigAutoField(primary_key=True)
    action_time = models.DateTimeField()
    username = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    stage = models.CharField(max_length=255)
    bot = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'user_actions'
