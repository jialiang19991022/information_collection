from django.shortcuts import render
from collection.models import information
from django.conf import settings

# Create your views here.

def index(request):
    if request.method == 'GET':
        return render(request,'collection/index.html')
    elif request.method == 'POST':
        form = information()
        form.stu_number = request.POST.get('stu_number')
        form.name = request.POST.get('name')
        form.phone_number = request.POST.get('phone_number')
        form.first_department = request.POST.get('first_department')
        form.second_department = request.POST.get('second_department')
        form.notes = request.POST.get('notes')
        form.experiences = request.POST.get('experiences')
        form.sex = request.POST.get('sex')
        form.major = request.POST.get('major')
        form.wishes = request.POST.get('wishes')
        form.QQ_number = request.POST.get('QQ_number')
        img = request.FILES.get('img')
        save_path = '{}/collection/{}.jpg'.format(settings.MEDIA_ROOT, form.stu_number)
        with open(save_path, 'wb') as f:
            for content in img.chunks(): 
                f.write(content)
        form.img = save_path
        form.save()
        return render(request,'collection/welcome.html')
    