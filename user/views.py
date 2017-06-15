# #-*- coding:utf-8 -*-
# from django.shortcuts import render
# from django.core.urlresolvers import reverse_lazy
# from django.views.generic.edit import FormView
# from django.contrib.auth import authenticate, login
# from user.forms import RegisterForm
#
#
# class RegisterView(FormView):
#     template_name = 'user/register.html'
#     form_class = RegisterForm
#     success_url = '/'
#
#     def form_valid(self, form):
#         form.save()
#         username = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password')
#         user = authenticate(username=username, password=password)
#         login(self.request, user)
#         return super(RegisterView, self).form_valid(form)


from django.shortcuts import render, redirect

from .forms import RegisterForm


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


