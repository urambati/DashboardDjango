
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>This is a music App</h1>")