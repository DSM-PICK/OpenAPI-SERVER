# views.py
import requests
from django.conf import settings
from django.http import JsonResponse

def school_schedule(request):
    key = request.GET.get('key')
    type_ = request.GET.get('type')
    page_index = request.GET.get('pageIndex')
    page_size = request.GET.get('pageSize')
    school_code = request.GET.get('schoolCode')
    atpt_code = request.GET.get('atptCode')
    started_ymd = request.GET.get('startedYmd')
    ended_ymd = request.GET.get('endedYmd')

    neis_url = settings.NEIS_URL+'/SchoolSchedule'
    params = {
        'key': key,
        'type': type_,
        'pIndex': page_index,
        'pSize': page_size,
        'SD_SCHUL_CODE': school_code,
        'ATPT_OFCDC_CODE': atpt_code,
        'AA_FROM_YMD': started_ymd,
        'AA_TO_YMD': ended_ymd
    }

    response = requests.get(neis_url, params=params)
    if response.status_code == 200:
        return JsonResponse(response.json())
    else:
        return JsonResponse({'error': 'Failed to fetch data from NEIS API'}, status=response.status_code)

 