from django.db import models

# Create your models here.
class DDeatils(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    d_id = models.CharField(db_column='D_ID', unique=True, max_length=200, blank=True)  # Field name made lowercase.
    d_name = models.CharField(db_column='D_Name', max_length=200, blank=True)  # Field name made lowercase.
    d_picurl = models.ImageField(upload_to='Photos/',null=True)  # Field name made lowercase.
    d_fathername = models.CharField(db_column='D_FatherName', max_length=255, blank=True)  # Field name made lowercase.
    d_address = models.TextField(db_column='D_Address', blank=True)  # Field name made lowercase.
    d_religion = models.CharField(db_column='D_Religion', max_length=150, blank=True)  # Field name made lowercase.
    d_maritalstatus = models.CharField(db_column='D_MaritalStatus', max_length=100, blank=True)  # Field name made lowercase.
    d_mobno = models.BigIntegerField(db_column='D_MobNo')  # Field name made lowercase.
    d_destination = models.CharField(db_column='D_Destination', max_length=150, blank=True)  # Field name made lowercase.
    d_duration = models.CharField(db_column='D_Duration', max_length=80, blank=True)  # Field name made lowercase.
    d_routeuse = models.CharField(db_column='D_RouteUse', max_length=150, blank=True)  # Field name made lowercase.
    d_placevislastyear = models.CharField(db_column='D_PlaceVisLastYear', max_length=50, blank=True)  # Field name made lowercase.
    d_familydeatils = models.JSONField(db_column='D_FamilyDeatils', blank=True, null=True)  # Field name made lowercase.
    d_deradetails = models.JSONField(db_column='D_DeraDetails', blank=True, null=True)  # Field name made lowercase.
    d_age = models.IntegerField(db_column='D_age', blank=True, null=True)  # Field name made lowercase.
    
    class Meta:
        managed = False
        db_table = 'd_deatils'

        
        
