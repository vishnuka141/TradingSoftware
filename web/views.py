from django.shortcuts import render
from django.views.decorators.cache import cache_control
from django.views.generic import TemplateView,FormView
from accounts.views import signin_required_user
from django.utils.decorators import method_decorator
# Create your views here.
# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
@method_decorator(signin_required_user,name="dispatch")
class QuotationView(TemplateView):
    template_name = 'quotation.html'
# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
@method_decorator(signin_required_user,name="dispatch")
class QuotationFormView(TemplateView):
    template_name = 'quotation-form.html'