from django.urls import path,include
from web import views
urlpatterns = [
  path('quotations/list',views.QuotationView.as_view(),name='q-list'),
  path('quotations/new',views.QuotationFormView.as_view(),name='q-new'),

]
