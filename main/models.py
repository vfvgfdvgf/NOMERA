from django.db import models
from django.contrib.auth.models import User

# ======= تصنيفات المقالات =======
class Category(models.Model):
    name = models.CharField(max_length=100)

    # SEO
    seo_title = models.CharField(max_length=70, blank=True, null=True)
    seo_description = models.CharField(max_length=160, blank=True, null=True)
    seo_keywords = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.name


# ======= المقالات =======
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    image_url = models.URLField(blank=True, null=True)
    published_date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # SEO
    seo_title = models.CharField(max_length=70, blank=True, null=True)
    seo_description = models.CharField(max_length=160, blank=True, null=True)
    seo_keywords = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.title

    # دالة مساعدة للقالب
    def author_name(self):
        if self.author:
            return self.author.get_full_name() or self.author.username
        return "إدارة الموقع"


# ======= الكويزات =======
class Quiz(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)

    # SEO
    seo_title = models.CharField(max_length=70, blank=True, null=True)
    seo_description = models.CharField(max_length=160, blank=True, null=True)
    seo_keywords = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        related_name='questions'
    )
    text = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.quiz.name} - {self.text[:30]}"


class Choice(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='choices'
    )
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.question.text[:30]} - {self.text}"


# ======= الكوبونات =======
class Coupon(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    store_link = models.URLField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)

    # SEO
    seo_title = models.CharField(max_length=70, blank=True, null=True)
    seo_description = models.CharField(max_length=160, blank=True, null=True)
    seo_keywords = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.name
