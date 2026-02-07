from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.views.decorators.cache import cache_page

from .models import Article, Category, Quiz, Coupon


# ==================================================
# 🏠 الصفحة الرئيسية
# ==================================================
@cache_page(60 * 5)  # كاش 5 دقائق
def home(request):
    context = {
        'latest_articles': Article.objects.order_by('-published_date')[:5],
        'latest_quizzes': Quiz.objects.order_by('-id')[:5],
        'latest_coupons': Coupon.objects.order_by('-expiry_date')[:5],
    }
    return render(request, 'main/home.html', context)


# ==================================================
# 📰 المقالات
# ==================================================
@cache_page(60 * 10)
def articles(request):
    categories = Category.objects.all()
    articles = Article.objects.order_by('-published_date')

    return render(request, 'main/articles.html', {
        'categories': categories,
        'articles': articles
    })


@cache_page(60 * 10)
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)

    return render(request, 'main/article_detail.html', {
        'article': article
    })


# ==================================================
# 📂 تصنيف المقالات
# ==================================================
@cache_page(60 * 10)
def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)

    articles = Article.objects.filter(
        category=category
    ).order_by('-published_date')

    return render(request, 'main/category_detail.html', {
        'category': category,
        'articles': articles,
        'articles_count': articles.count()
    })


# ==================================================
# 🧠 الكويزات
# ==================================================
from django.shortcuts import render, get_object_or_404
from .models import Quiz
from django.views.decorators.cache import cache_page


# صفحة عرض جميع الكويزات (عادي فيها كاش)
@cache_page(60 * 10)
def quizzes(request):
    quizzes = Quiz.objects.all()

    return render(request, 'main/quizzes.html', {
        'quizzes': quizzes
    })


# صفحة الكويز + حساب النتيجة (❌ بدون كاش)
def quiz_detail(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    questions = quiz.questions.all()

    score = 0
    total = questions.count()

    # ===============================
    # 🧮 حساب النتيجة
    # ===============================
    if request.method == "POST":
        for question in questions:
            selected_choice_id = request.POST.get(f"question_{question.id}")

            if selected_choice_id:
                try:
                    choice = question.choices.get(id=selected_choice_id)
                    if choice.is_correct:
                        score += 1
                except:
                    pass

        percentage = int((score / total) * 100) if total > 0 else 0

        return render(request, 'main/quiz_result.html', {
            'quiz': quiz,
            'score': score,
            'total': total,
            'percentage': percentage
        })

    # ===============================
    # عرض الكويز
    # ===============================
    return render(request, 'main/quiz_detail.html', {
        'quiz': quiz,
        'questions': questions
    })

# ==================================================
# 🧮 الحاسبات
# ==================================================
@cache_page(60 * 30)
def calculators(request):
    return render(request, 'main/calculators.html')


# ==================================================
# 🎟️ الكوبونات
# ==================================================
@cache_page(60 * 10)
def coupons(request):
    coupons = Coupon.objects.order_by('expiry_date')

    return render(request, 'main/coupons.html', {
        'coupons': coupons
    })


@cache_page(60 * 10)
def coupon_detail(request, pk):
    coupon = get_object_or_404(Coupon, pk=pk)

    return render(request, 'main/coupon_detail.html', {
        'coupon': coupon
    })


# ==================================================
# 🔍 البحث الشامل (مقالات + كويزات)
# ==================================================
@cache_page(60 * 2)
def global_search(request):
    query = request.GET.get('q', '').strip()

    articles = Article.objects.filter(
        Q(title__icontains=query) |
        Q(content__icontains=query)
    )

    quizzes = Quiz.objects.filter(
        Q(name__icontains=query) |
        Q(description__icontains=query)
    )

    return render(request, 'main/search_results.html', {
        'query': query,
        'articles': articles,
        'quizzes': quizzes
    })
# ==================================================
from .models import Article, Quiz, Category

from .models import Article, Quiz, Category, Coupon

def home(request):
    latest_articles = Article.objects.order_by('-created_at')[:10]
    latest_quizzes = Quiz.objects.order_by('-id')[:10]
    latest_coupons = Coupon.objects.order_by('-id')[:10]
    categories = Category.objects.all()

    return render(request, 'main/home.html', {
        'latest_articles': latest_articles,
        'latest_quizzes': latest_quizzes,
        'latest_coupons': latest_coupons,
        'categories': categories,
    })
