from django.db import models
from django.contrib.auth.models import User


class Family(models.Model):
    name        = models.CharField(max_length=100)
    created_by  = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_families')
    members     = models.ManyToManyField(User, related_name='families', blank=True)
    invite_code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Person(models.Model):
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]

    family    = models.ForeignKey(Family, on_delete=models.CASCADE, related_name='persons')
    name      = models.CharField(max_length=100)
    gender    = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    father    = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='children_from_father')
    mother    = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='children_from_mother')
    birth_date         = models.DateField(null=True, blank=True)
    bio                = models.TextField(blank=True)
    joined_by_marriage = models.BooleanField(default=False)
    added_by  = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='added_persons')
    claimed_by = models.ForeignKey(
    User, null=True, blank=True,
    on_delete=models.SET_NULL,
    related_name='claimed_persons'   # now returns multiple
)

    def __str__(self):
        return self.name


class Marriage(models.Model):
    spouse1       = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='marriages_as_spouse1')
    spouse2       = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='marriages_as_spouse2')
    marriage_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.spouse1} ❤️ {self.spouse2}"