from django.db import models
from djongo import models as m


class Cuanto(models.Model):
    _id = m.ObjectIdField()
    team_name = models.CharField(db_column='TeamName', max_length=50)
    cuanto_url = models.TextField(db_column='cuantoURL')
    db_ip = models.CharField(max_length=50)
    db_pass = models.CharField(max_length=50)
    db_user = models.CharField(max_length=50)
    db_port = models.CharField(max_length=10)
    db_name = models.CharField(max_length=50)
    db_connection_status = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'cuanto'
        app_label = 'cuanto'
