from django.db import models
from djutil.models import TimeStampedModel

# Create your models here.

class Report(TimeStampedModel):
    """
        Report Model
    """

    REPORTER_TYPE = (
        ('S', 'Survior'),
        ('F','Friend of survivor'),
        ('R','Relative of survivor'),
        ('X','Stranger'),
    )
    KNOWS_ASSAILANT = (
        ('Y', 'Yes'),
        ('N','No'),
    )
    INCIDENT_TYPE = (
        ('1', 'Eve Teasing'),
        ('2','Voyeurism'),
        ('3', 'Acid Violence'),
        ('4','Stalking'),
        ('5', 'Rape'),
        ('6','Disrobing'),
        ('7', 'Domestic Violence'),
        ('8','Marital Rape'),
        ('9', 'Child Molestation'),
    )
    reporter = models.CharField(max_length=1, choices=REPORTER_TYPE, default="")
    know_assailant = models.CharField(max_length=1, choices=KNOWS_ASSAILANT, default="")
    incident_type = models.CharField(max_length=1, choices=INCIDENT_TYPE, default="")
    location = models.TextField()
    time_of_incident = models.TimeField()
    date_of_incident = models.DateField()
    description = models.TimeField(blank=True,null=True)
    first_name = models.CharField(blank=True,null=True,max_length=50)
    last_name = models.CharField(blank=True,null=True,max_length=50)
    email = models.EmailField(blank=True,null=True,max_length=50)
    phone_number = models.CharField(blank=True,null=True,max_length=50)

    def __str__(self):              # __unicode__ on Python 2
        return self.description