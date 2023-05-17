from app.services import *
from app.models import Yandex_transaction_category as Category

def get_or_create_transaction_category(id, name):
    category_obj, created = Category.objects.get_or_create(category_id=id)
    category_obj.name = name.lower()
    category_obj.save()
    return category_obj

def get_transaction_category_id_by_name(name):
    query = Category.objects.filter(name=name)
    return query[0].category_id if query else None
