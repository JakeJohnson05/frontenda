from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect

from . import forms, models


def homeView(request):
  htmlVars = {
        'title': 'Frontenda',
        'posts': models.Post.objects.all()[::-1],
        'requestType': request,
        'firstRender': True,
    }

  if request.method == 'POST':
    htmlVars['highlightNew'] = True;
  else:
    htmlVars['highlightNew'] = False;




  return render(request, 'home.html', htmlVars)


def newPostView(request):
    htmlVars = {
        'title': 'Frontenda',
    }

    if request.method == 'POST':
        form = forms.newPostForm(request.POST)

        if form.is_valid():
            htmlVars['form'] = form
            form.save()
            return HttpResponseRedirect(reverse('frontendaClub:home'))
    else:
        form = forms.newPostForm()

    htmlVars['form'] = form
    return render(request, 'newPost.html', htmlVars)

def aboutView(request):

  return render(request, 'about.html')
