
from django.shortcuts import render
from django.views.decorators.cache import never_cache
from sentry.web.helpers import render_to_response

@never_cache
def login(request):
    return render(request, 'xorg_sentry/login.html')
