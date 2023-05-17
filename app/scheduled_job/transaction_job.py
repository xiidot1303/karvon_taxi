from app.services.yandex_api_service import get_transaction_category_list
from app.services.transaction_category_service import get_or_create_transaction_category
from app.models import Yandex_transaction_category as Category

def update_categories():
    categories = get_transaction_category_list()['categories']
    for category in categories:
        id = category['id']
        name = category['name']
        get_or_create_transaction_category(id, name)