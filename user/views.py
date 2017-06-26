from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm
from .models import UserProfile
from django.views.generic import DetailView
from django.views.generic.edit import FormView, CreateView
from django.views.generic import UpdateView
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from user.forms import SignatureForm
from PIL import Image
import time


# --用户中心--
class UserInfoView(DetailView):
    model = UserProfile
    template_name = 'user_info.html'
    context_object_name = 'info'
    pk_url_kwarg = 'user_id'

    def get_object(self, *args, **kwargs):
        obj = super(UserInfoView, self).get_object()
        return obj

    def get_context_data(self, **kwargs):
        context = super(UserInfoView, self).get_context_data(**kwargs)
        comment = self.object.comment_set.all()
        topic = self.object.topic_set.all()
        comment_nums = comment.count()
        topic_nums = topic.count()
        context.update({
            'topic_list': topic,
            'comment_list': comment,
            'comment_nums': comment_nums,
            'topic_nums': topic_nums
        })
        return context


# --用户注册--
def register(request):
    redirect_to = request.POST.get('next', request.GET.get('next', ''))
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            if redirect_to:
                return redirect(redirect_to)
            else:
                return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'user/register.html', context={'form': form, 'next': redirect_to})


# --更换签名--
def signaturechange(request):
    if request.method == 'POST':
        form = SignatureForm(request.POST)
        if form.is_valid():
            signature = form.cleaned_data['signature']
            info = UserProfile.objects.update(signature=signature)
            id = request.user.id
            return HttpResponseRedirect('/user_info/%s' % id)


# --更换头像--
def updateInfo(request):
    if request.method == 'POST':
        avatar = request.FILES['avatar']

        if avatar:
            avatartime = request.user.username + str(time.time()).split('.')[0]
            avatar_last = str(avatar).split('.')[-1]
            avatarname = 'user/img/%s.%s' % (avatartime, avatar_last)
            img = Image.open(avatar)
            if img.size[0] > img.size[1]:
                offset = int(img.size[0]-img.size[1])/2
                img = img.transform((img.size[1], img.size[1]), Image.EXTENT, (offset, 0, int(img.size[0]-offset), img.size[1]))
            else:
                offset = int(img.size[1] - img.size[0])/2
                img = img.transform((img.size[0], img.size[0]), Image.EXTENT, (0, offset, img.size[0], (img.size[1]-offset)))
            img.thumbnail((300, 300))
            img.save('media/' + avatarname)

            count = UserProfile.objects.filter(user=request.user).update(
                avatar=avatarname
            )
            id = request.user.id
            if count:
                return HttpResponseRedirect('/user_info/%s' % id)
            else:
                return HttpResponse('上传失败')
        return HttpResponse('图片为空')


