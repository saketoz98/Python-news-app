from django.db import models

# Create your models here.
class Category(models.Model):
    categories = (
     ('business','business'),
     ('entertainment','entertainment'),
     ('general','general'),
     ('health','health'),
     ('science','science'),
     ('sports','sports'),
     ('technology','technology')
     )
    country = (
     ('in','india'),
     ('us','us'),
     ('jp','jp'),
     ('gr','gr'),
     )

    category = models.CharField(max_length=50, choices=categories)
    country = models.CharField(max_length=50,choices = country)
