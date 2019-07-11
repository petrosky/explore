from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Widget
from .forms import AddWidget


def index(request):

    widgets = Widget.objects.all()

    context = {'widgets': widgets}
    return render(request, 'widgets/index.html', context)


def about(request):
    context = {}
    return render(request, 'widgets/about.html', context)


def detail(request, widget_id):
    widget = get_object_or_404(Widget, pk=widget_id)
    context = {'widget': widget}
    return render(request, 'widgets/detail.html', context)


def add(request):
    if request.method == 'POST':
        form = AddWidget(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your widget is added.')
            return redirect('home-index')
    else:
        form = AddWidget()
    return render(request, 'users/register.html', {'form': form})


def edit(request):
    pass


def delete(request):
    pass
