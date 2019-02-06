from django.shortcuts import render

from . import forms, models


def homeView(request):
    htmlVars = {
        'title': 'Frontenda',
    }

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
            return render(request, 'home.html', htmlVars)
    else:
        form = forms.newPostForm()

    htmlVars['form'] = form
    return render(request, 'newPost.html', htmlVars)

