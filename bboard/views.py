from django.shortcuts import render
from django.http import HttpResponse
from .models import Bb
from .models import Rubric
from django.template import loader
#def index(request):
#    return HttpResponse("Здесь будет выведен список обьявлений.")
#    s = 'Список обьявлений\r\n\r\n\r\n'
#    for bb in Bb.objects.order_by('-published'):
#        s += bb.title + '\r\n' + bb.content + '\r\n\r\n'
#    return HttpResponse(s, content_type='text/plain; charset=utf-8')
# Create your views here.

#def index(request):
#    template = loader.get_template('bboard/index.html')
#    bbs = Bb.objects.order_by('-published')
#    context = { 'bbs': bbs }
#    return HttpResponse(template.render(context, request))

def index(request):
    #bbs = Bb.objects.order_by('-published')
    bbs = Bb.objects.all()
    return render(request, 'bboard/index.html', {'bbs':bbs})

def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'rubrics':rubrics,
               'current_rubric': current_rubric}
    return render(request, 'bboard/by_rubric.html', context)