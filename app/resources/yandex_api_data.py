from config import YANDEX_CLIENT_ID

dirvers_list_data = {
    "fields": {
        "account": [
            "balance",
            "last_transaction_date",
        ],
        "car": [
            "callsign"
        ],
        "current_status": [
            "status"
        ],
        "driver_profile": [
            "id",
            "first_name",
            "last_name",
            "phones",
        ],
        "park": []
    },
    "query": {
        "park": {
            "id": YANDEX_CLIENT_ID,
        },
    },
    "sort_order": [
        {
            "direction": "asc",
            "field": "driver_profile.created_date"
        }
    ]
}

def create_transaction_data(amount, category_id, description, driver_profile_id):
    data = {
        "amount": str(amount),
        "category_id": category_id,
        "description": description,
        "driver_profile_id": driver_profile_id,
        "park_id": YANDEX_CLIENT_ID
    }
    return data

category_list_data={
    "query": {
        "category": {
            "is_creatable": True,
            "is_enabled": True
        },
        "park": {
            "id": YANDEX_CLIENT_ID
        }
    }

}