from PyPDF2 import PdfReader
from django.core.validators import FileExtensionValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)


class Author(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='images/', validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])])
    pdf = models.FileField(upload_to='pdf/', validators=[FileExtensionValidator(['pdf'])])
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    year = models.SmallIntegerField()
    price = models.PositiveIntegerField(blank=True, null=True)
    view_count = models.PositiveIntegerField(default=0)
    page_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    # def count_pages(self):
    #     with self.pdf.open('rb') as pdf_file:
    #         pdf_reader = PdfReader(pdf_file)
    #         return len(pdf_reader.pages)
    #
    # def save(self, *args, **kwargs):
    #     # self.page_count = self.count_pages()
    #     super().save(*args, **kwargs)