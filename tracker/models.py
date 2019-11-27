from django.db import models
from django.utils.translation import gettext as _

from django.db import models	
from django.utils.translation import gettext as _
class Sighting(models.Model):
    latitude = models.FloatField(
            help_text=_('Latitude of Sighting'),
    )
	
    longitude = models.FloatField(
	    help_text=_('Longitude of Sighting'),
    )
	
    squirrel_id = models.CharField(
            primary_key=True,
            max_length=32,
	    help_text=_('Unique Squirrel ID'),
    )
	
    AM = "AM"
    PM = "PM"
	
    SHIFT_CHOICES=(
            (AM,"AM"),
	    (PM,"PM"),
    )

    shift = models.CharField(
	    max_length=2,
	    choices=SHIFT_CHOICES,
	    default=AM,
	    help_text=_("Sighting session"),
    )
	
    date = models.DateField(
	    help_text=_("Sighting date"),
    )
	
    ADULT = "adult"
    JUVENILE = "juvenile"
	
    AGE_CHOICES =(
	    (ADULT,"Adult"),
	    (JUVENILE,"Juvenile"),
            ('',''),
    )
	
    age = models.CharField(
	    max_length=16,
	    choices=AGE_CHOICES,
	    default=ADULT,
	    help_text=_("Age of Squirrel"),
	    null=True,
    )
	
    GRAY="gray"
    BLACK="black"
    CINNAMON="cinnamon"
	
    FUR_CHOICES=(
            (GRAY,"Gray"),
	    (BLACK,"Black"),
	    (CINNAMON,"Cinnamon"),
	    ('',''),
    )
	
    fur_color = models.CharField(
            max_length=10,
	    choices=FUR_CHOICES,
	    default=GRAY,
	    help_text=_("Fur color of Squirrel"),
	    null=True,
    )
	
    GROUND_PLANE="ground_plane"
    ABOVE_GROUND="above_ground"
	
    LOC_CHOICES=(
	    (GROUND_PLANE,"Ground_Plane"),
	    (ABOVE_GROUND,"Above_Ground"),
            ('',''),
    )
	
    location = models.CharField(
	    max_length=20,
	    choices=LOC_CHOICES,
	    default=GROUND_PLANE,
	    help_text=_("Location of Squirrel"),
	    null=True,
    )
	
    specific_location = models.CharField(
	    max_length=20,
	    help_text=_("Specific location of Squirrel"),
	    null=True,
            blank=True,
    )
	
    running = models.BooleanField(
	    default=False,
    )
	
    chasing = models.BooleanField(
	    default=False,
    )
	
    climbing = models.BooleanField(
	    default=False,
    )
	
    eating = models.BooleanField(
	    default=False,
    )
	
    foraging = models.BooleanField(
	    default=False,
    )
	
    other_activities = models.CharField(
	    max_length=20,
	    help_text=_("Other activity"),
	    null=True,
            blank=True,
    )
	
    kuks = models.BooleanField(
	    default=False,
    )
	
    quaas = models.BooleanField(
	    default=False,
    )
	
    moans = models.BooleanField(
	    default=False,
    )

    tail_flags = models.BooleanField(
	    default=False,
    )
	
    tail_twitches = models.BooleanField(
	    default=False,
    )
	
    approaches = models.BooleanField(
	    default=False,
    )
	
    indifferent = models.BooleanField(
	    default=False,
    )
	
    runs_from = models.BooleanField(
	    default=False,
    )
