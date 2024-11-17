from django.db import models

# Create your models here.

#publisher class
class Publisher(models.Model):
    class Meta:
        db_table = "publisher"
    
    name = models.TextField(verbose_name="publisher name", unique=True)

    def __str__(self):
        return self.name
    
#university class
class University(models.Model):
    class Meta:
        db_table = "university"

    name = models.TextField(verbose_name="name", max_length=255)

    def __str__(self):
        return self.name

#author class
class Author(models.Model):
    class Meta:
        db_table = "author"
    
    first_name = models.TextField(verbose_name="first_name", max_length=255)
    last_name = models.TextField(verbose_name="last_name", max_length=255)
    affiliation = models.ManyToManyField(University, verbose_name="affiliation", blank=True, null=True)

    def __str__(self):
        return self.last_name


#paper class
class Paper(models.Model):
    class Mata:
        db_table = "paper"

    title = models.TextField(verbose_name="title", unique=True)
    publisher = models.ForeignKey(Publisher, verbose_name="publisher", blank=True, null=True, on_delete=models.PROTECT)
    authors = models.ManyToManyField(Author, verbose_name="author")
    arxiv = models.TextField(verbose_name="arxiv_id", blank=True, null=True, unique=True)
    doi = models.TextField(verbose_name="doi", blank=True, null=True, unique=True)
    published_date = models.DateField(verbose_name="published_date")

    def __str__(self):
        return self.title
    