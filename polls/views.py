from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice #.(현재폴더)의 models를 참조 후 임폴트

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:10] # '-'는 역순 옵션! / list 형태로 나오진 않음
    output = ','.join([q.question_text for q in latest_question_list]) #리스트를 join으로 합침(split 반대개념)
    # return HttpResponse("Hello, world. You're at the polls index.")
    # return HttpResponse(output)
    name = request.POST.get('qstname')
    new = Question.objects.get(pk=name)
    new.save()
    return render(request, 'polls/index.html', {'latest_question_list':latest_question_list}) #dictionary 형태로 넘김
def detail(request, question_id): # 질문 상세 페이지
    question = Question.objects.get(pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id): # 투표 결과 페이지 /urls.py의 question_id
    q = Question.objects.get(pk=question_id)
    votes = q.choice_set.all() #_set.all() : get된 키와 일치하는 모든 외래키
    #votes = q.objects.filter(question=question)
    return render(request, 'polls/result.html', {'votes':votes})

def vote(request, question_id): # 투표 페이지
    num = request.POST['choice'] #보기번호 (detail.html radio의 name)
    choice = Choice.objects.get(pk=num)
    vote = choice.votes + 1 #투표수 1증가
    choice.votes =vote
    # choice.votes += 1
    choice.save()
    return HttpResponse("You're voting on question %s." % question_id)

def free(request):
    return render(request, 'polls/freelancer.html', {})