from django.db import models

# Create your models here.


class Math(models.Model):
    # OP_CHOICES = (
    #     ('add', 'adding'),
    #     ('mul', 'mul'),
    #     ('sub', 'sub'),
    #     ('div', 'div'),
    # )
    class OpChoices(models.TextChoices):
        ADD = 'add'
        SUB = 'sub'
        MUL = 'mul'
        DIV = 'div'

    op = models.CharField(max_length=3, choices=OpChoices.choices)
    a = models.IntegerField()
    b = models.IntegerField()
    result = models.FloatField(null=True, blank=True)