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


# alohida proect portfolioga aloqasi yo'q
# class Users(models.Model):
#     tg_id = models.BigIntegerField()
#     full_name = models.CharField(max_length=255)
#     username = models.CharField(max_length=255)
#     first_name = models.CharField(max_length=255)
#     daily_score = models.IntegerField()
#
#
# class Category(models.Model):
#     nomi = models.CharField(max_length=155)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.nomi
#
#
# class Savollar(models.Model):
#     category = models.ForeignKey(Category, related_name='all_category', on_delete=models.CASCADE)
#     savol = models.CharField(max_length=255)
#     manbaa = models.CharField(max_length=255)
#     javob_1 = models.CharField(max_length=55)
#     javob_2 = models.CharField(max_length=55)
#     javob_3 = models.CharField(max_length=55, null=True, blank=True)
#     javob_4 = models.CharField(max_length=55, null=True, blank=True)
#     FRESHMAN = '1'
#     SOPHOMORE = '2'
#     JUNIOR = '3'
#     SENIOR = '4'
#     YEAR_IN_SCHOOL_CHOICES = [
#         (FRESHMAN, '1'),
#         (SOPHOMORE, '2'),
#         (JUNIOR, '3'),
#         (SENIOR, '4'),
#     ]
#     javobi = models.CharField(
#         max_length=2,
#         choices=YEAR_IN_SCHOOL_CHOICES,
#         default=FRESHMAN,
#     )
#     image = models.ImageField(null=True, blank=True)
#
#     def __str__(self):
#         return self.savol
