from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from api.myApi.models import Professor, Student, Classe, Subject, Promotion


@csrf_exempt
def professorDetails(request,pk):

    return ;

def professors(request):
    return ;

def promotionDetails(request):
    return ;

def promotions(request):
    return ;

def studentDetails(request):
    return ;

def students(request):
    return ;

def subjects(request):
    return ;

def subjectDetails(request):
    return ;

def classeDetails(request):
    return ;

def classes(request):
    return ;