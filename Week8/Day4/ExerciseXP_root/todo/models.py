from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    image=models.URLField()

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('category', args = [self.id])

class Todo(models.Model):
    title= models.CharField(max_length=50)
    details=models.TextField()
    has_been_done= models.BooleanField(default=False)
    date_creation=models.DateField(auto_now_add=True)
    date_comletion= models.DateField(null=True)
    deadline_date= models.DateField()
    category =models.ForeignKey(Category, related_name='todos',on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title