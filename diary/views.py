from django.shortcuts import render
from diary.models import Memory
# Create your views here.

def diaryindex(request):
    #전체 포스팅을 가져올 준비 , 아직 가져오지는 않음.
    diary_qs = Memory.objects.all().order_by("-id") #id필드에 대한 역순 정렬 (최신순)
    return render(request,"diary/d_index.html",{
        "diarypost_list": diary_qs
    })
