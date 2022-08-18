from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name

class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        same_dir = Director.objects.filter(first_name = self.first_name, last_name = self.last_name)
        if same_dir.exists():
            raise ValidationError("Can't add duplicate")
        else:
            super(Director, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name

    def get_absolute_url(self):
        return reverse('director_films', args=[self.id])

class Film(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    created_in_country = models.ForeignKey(Country, null=True, on_delete=models.SET_NULL)
    available_in_countries = models.ManyToManyField(Country, related_name='films')
    categories = models.ManyToManyField(Category, related_name='films')
    directors = models.ManyToManyField(Director, related_name='films')

    def __str__(self) -> str:
        out = f"""
        {self.title}
        {self.release_date}
        Category:
        """
        for category in self.categories.all():
            out += f"\n{str(category)}"
        out += "\nDirector"
        for dir in self.directors.all():
            out += f"\n{str(dir)}"
        out += f"\nReleased: {self.release_date}"        
        return out