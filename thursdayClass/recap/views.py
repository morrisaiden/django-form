from django.shortcuts import render, redirect
from django.forms import modelform_factory

from recap.models import Person, Schedule


# Create your views here.

def recaped(request, id):
    recap_class = Person.objects.get(pk=id)
    return render(request, "website/recap.html", {"huawei": recap_class})


# def home(request):
#     # revision = Schedule.object.all()
#     return render(request, 'website/home.html')

def home(request):
    if request.method == 'POST':
        revision = Schedule.objects.all()
        return redirect('results', revision=revision)
        context = {"revision": revision}
    return render(request, 'website/home.html', context)


ScheduleMeeting = modelform_factory(Schedule, exclude=[])


def newpage(request, form=None):
    if request.method == "POST":
        form = ScheduleMeeting(request.POST)
        if form.is_valid():
            form.save()
            # return redirect("")
    else:
        form = ScheduleMeeting()
    return render(request, 'website/new.html', {'form': form})


def results(request, revisions):
    context = {"revisions": revisions}

    return render(request, 'website/results.html', context)
