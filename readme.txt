Django's Object-Relational Mapping (ORM) is a powerful feature that allows developers to 
interact with the database using Python code instead of writing raw SQL queries. 


This abstraction layer simplifies database operations and improves code readability. 
Below is a comprehensive overview of Django ORM, including basic concepts, queries, and examples.

Basic Concepts
Models: In Django, each database table is represented by a model class. 
Each model class corresponds to a single table, 
and each attribute of the class represents a field in the table.

Migrations: Migrations are how Django manages database schema changes. 
When you create or modify models, 
you generate migrations to update the database schema accordingly.

QuerySets: A QuerySet is a collection of database queries that Django ORM allows you to create. 
You can retrieve, filter, and manipulate data using QuerySets.


from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    
    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    reviewer_name = models.CharField(max_length=100)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reviewer_name} - {self.book.title}"
