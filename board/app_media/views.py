from multiprocessing import context
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from .forms import UploadFileForm, UploadValidFile


def upload_file(request):
    if request.method == 'POST':
        upload_file_form = UploadFileForm(request.POST, request.FILES)
        if upload_file_form.is_valid():
            file = request.FILES['file']
            return HttpResponse(content=(file.name, f' {file.size} byte'), status=200)
    else:
        upload_file_form = UploadFileForm()

    context = {
        'form': upload_file_form
    }
    return render(request, 'upload_file.html', context=context)


def upload_valid_file(request):
    if request.method == 'POST':
        upload_file_form = UploadValidFile(request.POST, request.FILES)
        if upload_file_form.is_valid():
            a = upload_file_form
            file = request.FILES['file']
            for line in file:
                b = line.decode('utf-8')
                if b.startswith('word') or b.endswith('word'):
                    print('forbidden word!')
                    return HttpResponse(f'Файл не прошел проверку.')
            return HttpResponse(content=(file.name, f' {file.size} byte'), status=200)
        else:
            return HttpResponseBadRequest()
    else:
        upload_file_form = UploadValidFile()

    context = {
        'form': upload_file_form
    }
    return render(request, 'upload_file.html', context=context)
