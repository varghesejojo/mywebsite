from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from . models import Msg
from django.contrib import messages
import os
# Create your views here.



from django.http import HttpResponse
import os

def download_file(request):
    file_path = os.path.join('static/media/myfile.pdf')  # Replace with the actual file path
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            return response
    else:
        return HttpResponse('File not found.')




def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        msg=Msg(name=name, email=email, phone=phone, message=message)
        msg.save()
        messages.success(request, 'Contact added successfully!')
    return render(request, 'index.html')