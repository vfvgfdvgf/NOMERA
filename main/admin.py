import nested_admin
from django.contrib import admin
from .models import Category, Article, Quiz, Question, Choice, Coupon


# ========= إدارة تصنيفات المقالات =========
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


# ========= إدارة المقالات =========
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'published_date')
    list_filter = ('category',)
    search_fields = ('title', 'content')
    ordering = ('-published_date',)


# ========= إدارة الكويزات (Nested Admin) =========

# اختيارات السؤال
class ChoiceInline(nested_admin.NestedTabularInline):
    model = Choice
    extra = 3
    min_num = 2  # أقل عدد خيارات
    max_num = 6  # حد أقصى (اختياري)


# الأسئلة داخل الكويز
class QuestionInline(nested_admin.NestedStackedInline):
    model = Question
    extra = 1
    inlines = [ChoiceInline]
    show_change_link = True


# الكويز
@admin.register(Quiz)
class QuizAdmin(nested_admin.NestedModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    inlines = [QuestionInline]


# ========= إدارة الأسئلة (منفصلة - احتياط) =========
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'quiz')
    list_filter = ('quiz',)
    search_fields = ('text',)
    inlines = [ChoiceInline]


# ========= إدارة الكوبونات =========
@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'expiry_date')
    search_fields = ('name', 'code')
    list_filter = ('expiry_date',)
