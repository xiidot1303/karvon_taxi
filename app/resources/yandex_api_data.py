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