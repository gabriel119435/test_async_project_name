import asyncio
from functools import wraps

from django.http import HttpResponseNotAllowed
from django.utils.log import log_response


def _require_http_methods(request_method_list):
    def decorator(func):
        def not_allowed(request):
            response = HttpResponseNotAllowed(request_method_list)
            log_response(
                "method not allowed (%s): %s",
                request.method,
                request.path,
                response=response,
                request=request,
            )
            return response

        def inner(request, *args, **kwargs):
            if request.method not in request_method_list:
                return not_allowed(request)
            return func(request, *args, **kwargs)

        async def a_inner(request, *args, **kwargs):
            if request.method not in request_method_list:
                return not_allowed(request)
            return await func(request, *args, **kwargs)

        return wraps(func)(a_inner if asyncio.iscoroutinefunction(func) else inner)

    return decorator


custom_require_GET = _require_http_methods(["GET"])
