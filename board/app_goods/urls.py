from django.urls import path
from .views import item_list, update_prices, new_item_list, new_upd_prices, model_form_upload, upload_files

urlpatterns = [
    path('items/', item_list, name='item_list'),
    path('new_items/', new_item_list, name='new_items_list'),
    path('update_prices/', update_prices, name='update_prices'),
    path('new_upd/', new_upd_prices, name='new_upd_prices'),
    path('model_form_upd/', model_form_upload, name='model_form_upload'),
    path('upload_files/', upload_files, name='upload_files')
]
