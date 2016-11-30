from django.db import models

# Create your models here.


class Entry(models.Model):
    title = models.CharField(max_length=500)
    author = models.ForeignKey('auth.user')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now_add=True, editable=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "entries"
