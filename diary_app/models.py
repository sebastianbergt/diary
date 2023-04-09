from django.db import models

class DiaryEntry(models.Model):
    date = models.DateField(auto_now_add=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.date}: {self.content[:50]}'
