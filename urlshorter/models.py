from django.db import models

class URLShorter(models.Model):
    url = models.CharField(max_length=500, verbose_name="URL")
    shorter = models.CharField(max_length=8, verbose_name="Shorter")

    class Meta:
        verbose_name="URLSorter"
        verbose_name_plural="URLSorters"

