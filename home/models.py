from django.db import models


class Help(models.Model):
    """
    A model for admin to edit and add FAQ
    """
    class Meta:
        verbose_name_plural = 'Help'

    question = models.CharField(max_length=254)
    answer = models.TextField()

    def __str__(self):
        return self.question
