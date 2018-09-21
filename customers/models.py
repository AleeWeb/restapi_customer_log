from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Customer(models.Model):
    purchase_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100, blank=True, default='')
    last_name = models.CharField(max_length=100, blank=True, default='')
    purchase_item = models.CharField(max_length=100, blank=True, default='')
    price_total = models.IntegerField()

    class Meta:
        ordering = ('purchase_date',)

    def __str__(self):
        return self.purchase_item