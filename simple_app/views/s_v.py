import json
from http import HTTPStatus

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET

from simple_app.custom_async.csrf import both_csrf_exempt
from simple_app.custom_async.http_require import custom_require_GET
from simple_app.services.s_svc import read, create, delete, read_slow


@csrf_exempt
@both_csrf_exempt
def dev(request):
    if request.method == "GET":
        return JsonResponse(read(), safe=False)

    elif request.method == "POST":
        dev_dict = json.loads(request.body)
        return JsonResponse(create(dev_dict), status=HTTPStatus.CREATED, safe=False)

    elif request.method == "DELETE":
        pk = request.GET.get('id')
        delete(pk)
        return JsonResponse({"deleted": pk}, safe=False)

    else:
        return JsonResponse({"error": f"verb {request.method} not accepted"}, status=HTTPStatus.BAD_REQUEST)


@csrf_exempt
@both_csrf_exempt
@require_GET
@custom_require_GET
def slow_filter(request):
    return JsonResponse(read_slow(), safe=False)
