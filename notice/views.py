from django.shortcuts import render,redirect
from .models import Notice
from django.utils import timezone

# Create your views here.
def home(request):
    notices = Notice.objects
    return render(request,'home.html',{'notices':notices})

def detail(request, notice_id):
    notice_detail = Notice.objects.get(id=notice_id)
    return render(request, 'detail.html', {'notice': notice_detail})

def new(request):
    return render(request, 'new.html')

def create(request):
    notice = Notice()
    notice.title = request.GET['title']
    notice.body = request.GET['body']
    notice.pub_date = timezone.datetime.now()
    notice.save()
    return redirect('/notice/' + str(notice.id))

def delete(request, notice_id):
    Notice.objects.get(id=notice_id).delete()
    return redirect('/')

def edit(request, notice_id):
    notice = Notice.objects.get(id=notice_id)
    return render(request, 'edit.html', {'notice':notice})

def update(request, notice_id):
    notice = Notice.objects.get(id=notice_id)
    notice.title =request.POST.get('title')
    notice.body =request.POST.get('body')
    notice.pub_date = timezone.datetime.now()
    notice.save()
    return redirect('/notice/' + str(notice.id))

def about(request):
    return render(request, 'about.html')