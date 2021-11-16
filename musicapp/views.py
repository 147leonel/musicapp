from django.shortcuts import render
from .forms import MusicForm
# Create your views here.
def new_music(request):
    if request.method == "POST":
        form = MusicForm(request.POST)
        if form.is_valid():
            Music = form.save(commit=False)
            Music.save()
    else:
        form = MusicForm()
    return render(request, 'musicapp/new_music.html', {'form': form})