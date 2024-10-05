from django.urls import path
from main.views import magaz, main, pronas, bsket_add, katalog, resume, kontakt


app_name = 'main'

urlpatterns = [
    path('katalog/', katalog, name="katalog"),
    path("", main, name='main'),
    path("pronas/", pronas, name='pronas'),
    path('magaz/', magaz, name="magaz"),
    path('magaz/category/<int:category_id>/', magaz, name="category"),
    path('magaz/page/<int:page>/', magaz, name="paginator"),
    path('bskets/add/<int:product_id>/', bsket_add, name="bsket_add"),
    path('resume/<int:product_id>/', resume, name="resume"),
    path('kontakt/', kontakt, name="kontakt")
    
]