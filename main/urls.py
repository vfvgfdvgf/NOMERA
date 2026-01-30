from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),

    # الحاسبات
    path('calculators/', views.calculators, name='calculators'),

    # المقالات
    path('articles/', views.articles, name='articles'),
    path('articles/<int:pk>/', views.article_detail, name='article_detail'),

    # الكويزات
    path('quizzes/', views.quizzes, name='quizzes'),
    path('quizzes/<int:pk>/', views.quiz_detail, name='quiz_detail'),
     # الكوبونات
    path('coupons/', views.coupons, name='coupons'),
    path('coupons/<int:pk>/', views.coupon_detail, name='coupon_detail'),
    path('categories/<int:pk>/', views.category_detail, name='category_detail'),
    path('search/', views.global_search, name='global_search'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
