from django.db import models

YEAR_IN_SCHOOL_CHOICE = [
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
    ('GR', 'Graduate'),
]

SHIRT_SIZE = [
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
]


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    shirt_sizes = models.CharField(choices=SHIRT_SIZE, max_length=1)

    def __str__(self) -> str:
        return f"{self.first_name} - {self.last_name} - {self.shirt_sizes}"


class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_starts = models.IntegerField(default=0)


class Runner(models.Model):
    MedalType = models.TextChoices('Media type', 'GOLD SILVER BRONZE')
    name = models.CharField(max_length=50)
    medal = models.CharField(max_length=10, choices=MedalType.choices, blank=True)


"""
  Les relations django plusieurs-à-un
"""


class Manufacture(models.Model):
    pass


class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacture, on_delete=models.SET_NULL, null=True, blank=True)


"""
  Les relations plusieurs-à-plusieurs
"""


class Topping(models.Model):
    # pizzas = models.ManyToManyField("Pizza", related_name="Pizza_Topping")
    pass


class Pizza(models.Model):
    toppings = models.ManyToManyField(Topping, related_name="Pizza_Topping")


"""
    Django ajouter des champs supplémentaires dans les relations many to many field example
"""


class Artist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.name}"


class Group(models.Model):
    name = models.CharField(max_length=100)
    artists = models.ManyToManyField(Artist, through="MemberShip")

    def __str__(self):
        return f"{self.name} - {self.artists}"


class MemberShip(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateTimeField()
    invite_reason = models.CharField(max_length=100)


"""
    Comment modéliser l'héritage simple example
"""


class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=False, blank=False)

    class Meta:
        abstract = True
        ordering = ['name', ]


class Unmanaged(models.Model):
    field = models.TextField()

    class Meta:
        abstract = True
        managed = True


class Student(CommonInfo, Unmanaged):
    home_group = models.CharField(max_length=5)

    class Meta(CommonInfo.Meta, Unmanaged.Meta):
        verbose_name = "Student"
        db_table = "Student"


"""
    Comment modéliser l'héritage multiple example
"""


class Place(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    class Meta:
        ordering = ['name', ]
        db_table = "Place"


class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    class Meta:
        ordering = ['name', ]
        db_table = 'Restaurant'


"""
 Encore de l'héritage multiple à l'exemple
"""


class Article(models.Model):
    article_id = models.AutoField(primary_key=True)

    class Meta:
        ordering = ['article_id']
        db_table = 'Article'


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)

    class Meta:
        ordering = ['book_id', ]
        db_table = 'Book'


class BookReview(Article, Book):
    registered_date = models.DateField()

    class Meta:
        ordering = ['registered_date', ]
        db_table = 'BookReview'
