from django.db import models

# Create your models here.
class Invite(models.Model):
    name = models.CharField(max_length=500)
    branch = models.CharField(max_length=500)
    GENDER_CHOICES = (
      ("M", "Male"),
      ("F", "Female"),
      ("?", "Unknown")
    )
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default="?"
    )
    date_of_birth = models.DateField(blank=True, null=True)
    RACE_CHOICES = (
        ("ASIAN", "Asian"),
        ("BLACK", "Black"),
        ("LATINO", "Latino"),
        ("WHITE", "White"),
        ("OTHER", "Other"),
        ("?", "Unknown"),
    )
    race = models.CharField(
        max_length=10,
        choices=RACE_CHOICES,
        default="?"
    )
    REPORTERS = (
        ("lois-lane", "Lois Lane"),
        ("clark-kent", "Clark Kent"),
        ("jimmy-olson", "Jimmy Olson") 
    )
    reporter = models.CharField(
        max_length=255,
        choices=REPORTERS,
        blank=True,
        null=True
    )
