from django.db import models

class Member(models.Model):
    CATEGORIES =[
        ('Infant', 'Infant'),
        ('Junior', 'Junior'),
        ('Adult', 'Adult'),
        ('Senior', 'Senior'),
    ]
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    phone = models.IntegerField()
    birth_date = models.DateField()
    category = models.CharField(max_length=20, choices=CATEGORIES)

    def __str__(self):
        return self.full_name
    
class Court(models.Model):
    TYPES = [
        ('t', 'Tenis'),
        ('p', 'Pádel'),
    ]
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=50)
    type = models.CharField(max_length=1, choices=TYPES)

    def __str__(self):
        return self.description
    
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.member.full_name} - {self.court.description} - {self.date}"