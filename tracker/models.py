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
    )

    age = models.CharField(
            max_length=16,
            choices=AGE_CHOICES,
            default=ADULT,
            help_text=_("Age of Squirrel"),
    )

    GRAY="gray"
    BLACK="black"
    CINNAMON="Cinnamon"
    
    FUR_CHOICES=(
            (GRAY,"Gray"),
            (BLACK,"Black"),
            (CINNAMON,"Cinnamon"),
    )

    fur_color = models.CharField(
            max_length=10,
            choices=FUR_CHOICES,
            default=GRAY,
            help_text=_("Fur color of Squirrel"),
    )

    GROUND_PLANE="ground_plane"
    ABOVE_GROUND="above_ground"

    LOC_CHOICES=(
        (GROUND_PLANE,"Ground_Plane"),
        (ABOVE_GROUND,"Above_Ground"),
    )

    location = models.CharField(
            max_length=20,
            choices=LOC_CHOICES,
            default=GROUND_PLANE,
            help_text=_("Location of Squirrel"),
    )

