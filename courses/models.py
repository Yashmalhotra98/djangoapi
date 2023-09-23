from django.db import models

# Create your models here.
class Course(models.Model):
    #  We're currently using swlite database that comes with Django
    name = models.CharField(max_length=200) # CharField Stands for Character Fields in Django Data types or SQL Data types like Char, Varchar, etc.
    language = models.CharField(max_length=200)
    price = models.CharField(max_length=10)

    def __str__(self):
        #  Self here is nothing but our Course class and we're accessing the name object/variable inside the name class.
        return self.name

#  Our model is pretty much done here, now we need to make a migration and then push the migration into the data base.
#  The Django stuff completes here.

