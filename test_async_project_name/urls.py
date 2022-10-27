from django.urls import path

from simple_app.views import simple, s_v, a_v

urlpatterns = [
    path('a/', simple.a),
    path('b/', simple.b),
    path('c/', simple.c),
    path('d/', simple.d),
    path('bad/', simple.bad),

    path('dev/', s_v.dev),
    path('adev/', a_v.dev),

    path('slow_dev/', s_v.slow_filter),
    path('aslow_dev/', a_v.slow_filter),

]
