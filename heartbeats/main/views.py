"""doc string"""
from django.shortcuts import render
from .forms import DocumentForm
from .functions.functions import handle_uploaded_file

# Create your views here.
def index(request):
    """Home Page"""
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return render(request, 'main/music_player.html')
    else:
        form = DocumentForm()
    return render(request, 'main/index.html', {'form':form})


def termsofservice(request):
    """Terms of Service Page"""
    return render(request, 'main/termsofservice.html')


def privacypolicy(request):
    """Privacy Policy Page"""
    return render(request, 'main/privacypolicy.html')
