from _csv import reader
from decimal import Decimal
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Item, NewItem, File
from .forms import UploadPriceForm, NewUploadForm, DocumentForm, MultiFileForm
import datetime


def item_list(request):
    items = Item.objects.all()
    return render(request, 'items_list.html', {'items_list': items})


def new_item_list(request):
    items = NewItem.objects.all()
    return render(request, 'new_items_list.html', {'items_list': items})


def update_prices(request):
    if request.method == 'POST':
        upload_file_form = UploadPriceForm(request.POST, request.FILES)
        if upload_file_form.is_valid():
            price_file = upload_file_form.cleaned_data['file'].read()
            price_str = price_file.decode('utf-8').split('\n')
            csv_reader = reader(price_str, delimiter=",", quotechar='"')
            for row in csv_reader:
                try:
                    print(row)
                    print(row[0], row[1])
                    Item.objects.filter(code=row[0]).update(price=Decimal(row[1]))
                except IndexError:
                    return HttpResponse(content='Please check you file!', status=200)
            return HttpResponse(content='Цены были успешно обновлены', status=200)
    else:
        upload_file_form = UploadPriceForm()

    context = {
        'form': upload_file_form
    }
    return render(request, 'upload_price_file.html', context=context)


def new_upd_prices(request):
    if request.method == 'POST':
        upload_file_form = NewUploadForm(request.POST, request.FILES)
        upload_file = DocumentForm(request.POST, request.FILES)
        if upload_file_form.is_valid():
            price_file = upload_file_form.cleaned_data['file'].read()
            price_str = price_file.decode('utf-8').split('\n')
            csv_reader = reader(price_str, delimiter=":", quotechar='"')
            count_rows = 0
            not_upd_rows_count = 0
            for row in csv_reader:
                try:
                    print(row)
                    NewItem.objects.filter(code=row[0]).update(price=Decimal(row[1]))
                    count_rows += 1
                except:
                    not_upd_rows_count += 1

            if upload_file.is_valid():
                upload_file.save()

            return HttpResponse(content=f'Цены были успешно обновлены, в количестве {count_rows}, '
                                        f'пропущено {not_upd_rows_count} товаров', status=200)
    else:
        upload_file_form = NewUploadForm()

    context = {
        'form': upload_file_form
    }
    return render(request, 'upload_price_file.html', context=context)


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = DocumentForm()
    return render(request, 'file_form_upload.html', {'form': form})


def upload_files(request):
    if request.method == 'POST':
        form = MultiFileForm(request.POST, request.FILES)
        if form.is_valid():
            files = request.FILES.getlist('file_field')
            for f in files:
                instance = File(file=f)
                instance.save()
            return redirect('/')
    else:
        form = DocumentForm()
    return render(request, 'file_form_upload.html', {'form': form})