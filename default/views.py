from django.shortcuts import render, render_to_response
from django.views.generic import ListView, DetailView, RedirectView, CreateView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *

# Create your views here.
def poll_list(req):
    polls = Poll.objects.all()
    return render_to_response('poll_list.html',{'polls':polls})


class PollList(ListView):
    model = Poll

class PollDetail(DetailView):
    model = Poll
    # 取得額外資料供頁面範本顯示
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        options = Option.objects.filter(poll_id=self.kwargs['pk'])
        context['options'] = options
        return context

class PollVote(RedirectView):
    def get_redirect_url(self, **kwargs):
        opt = Option.objects.get(id=self.kwargs['oid'])
        opt.count+=1
        opt.save() 
        return "/poll/{}/".format(opt.poll_id)

## 新增投票主題
class PollCreate(CreateView):
    model = Poll
    fields = ['subject']    # 指定要顯示的欄位
    success_url = '/poll/'  # 成功新增後要導向的路徑
    template_name = 'general_form.html' # 要使用的頁面範本

## 修改投票選項
class  PollUpdate(UpdateView):
    model = Option
    fields = ['title']
    template_name = 'general_form.html'
    # 修改成功後返回其所屬投票主題檢視頁面
    def get_success_url(self):
        return '/poll/'+str(self.object.poll_id)+'/'