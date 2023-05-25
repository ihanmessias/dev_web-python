from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

# id (primary key - Automática)
# first_name (string), last_name (string), phone (string)
# email (email), created_date (date), description (text

#### >  Part II :
# category (foreign key), show (boolean), owner (foreign key)
# picture (imagem)


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name
    
# Tabela Contact:
class Contact(models.Model):
    
    first_name = models.CharField(max_length=14, blank=True)
    last_name = models.CharField(max_length=14, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='Pictures/%Y/%m/')
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,blank=True,null=True)
    owner = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'