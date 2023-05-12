from app.views import *
from django.http import JsonResponse
from config import CLICK_SERVICE_ID
from app.services.driver_service import get_driver_by_callsign
from django.views.decorators.csrf import csrf_exempt



def create_response_data(error=0, error_note="Success", params=None):
    data = {     
        "error": error,
        "error_note": error_note,
    }
    if params:
        data["params"] = params
    return data

@csrf_exempt
def send_profile_info(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            error, error_note, params = 0, "Success", None
            # get values from data
            action = data["action"]
            service_id = data["service_id"]
            callsign = data['params']['callsign']
            # check service ID and action
            if int(action) == 0 and int(service_id) == int(CLICK_SERVICE_ID):
                # get driver
                if driver:=get_driver_by_callsign(callsign):
                    params = {
                        "name": f"{driver.last_name} {driver.first_name}",
                        "phone": driver.phone,
                        "id": driver.profile_id
                    }
                else:
                    # driver does not exist
                    error, error_note = -5, "Haydovchi mavjud emas"
            else:
                error, error_note = -1, "Service ID yoki action xato"
        except Exception as ex:
            print(ex)
            error, error_note = -8, "Error"
        data = create_response_data(error, error_note, params)
        response = JsonResponse(data=data)
        response['Content-Type'] = 'application/json'
        response['Charset'] = 'utf-8'
        return response
    else:
        HttpResponse('')