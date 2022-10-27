import json
from http import HTTPStatus

from django.http import JsonResponse

from simple_app.custom_async.csrf import both_csrf_exempt
from simple_app.custom_async.http_require import custom_require_GET
from simple_app.services.a_svc import read, create, delete, a_read_slow, read_slow_but_fast


@both_csrf_exempt
async def dev(request):
    if request.method == "GET":
        return JsonResponse(await read(), safe=False)

    elif request.method == "POST":
        dev_dict = json.loads(request.body)
        return JsonResponse(await create(dev_dict), status=HTTPStatus.CREATED, safe=False)

    elif request.method == "DELETE":
        pk = request.GET.get('id')
        await delete(pk)
        return JsonResponse({"deleted": pk}, safe=False)

    else:
        return JsonResponse({"error": f"verb {request.method} not accepted"}, status=HTTPStatus.BAD_REQUEST)


@both_csrf_exempt
@custom_require_GET
async def slow_filter(request):
    return JsonResponse(await a_read_slow(), safe=False)
    # return JsonResponse(await read_slow_but_fast(), safe=False)
