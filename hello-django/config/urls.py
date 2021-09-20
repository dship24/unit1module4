from django.contrib import admin
from django.urls import path
from app.views import hello_view, hey_name, birthday, burber, near_hundred, string_splosion, cat_dog,lone_sum

urlpatterns = [
    path('hello/', hello_view),
    path('age-in/<int:end>/<int:birthyear>', birthday),
    path('order-total/<int:burgers>/<int:fries>/<int:drinks>', burber),
    path('warmup-1/near-hundred/<int:n>/', near_hundred),
    path('warmup-2/string-splosion/<str>/', string_splosion),
    path('string-2/cat_dog/<str>/', cat_dog),
    path('logic-2/lone-sum/<int:a>/<int:b>/<int:c>/', lone_sum),
    path('hey/<name>', hey_name),
    path('admin/', admin.site.urls),
]
