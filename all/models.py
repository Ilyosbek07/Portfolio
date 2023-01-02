from django.db import models


class PortfolioModel(models.Model):
    name = models.CharField(max_length=55, null=True, blank=True)
    description = models.CharField(max_length=55, null=True, blank=True)
    # images = models.ImageField()
    link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ReviewsModel(models.Model):
    name = models.CharField(max_length=155)
    job = models.CharField(max_length=55)
    # image = models.ImageField()
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ContactModel(models.Model):
    name = models.CharField(max_length=155, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    subject = models.CharField(max_length=155, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
