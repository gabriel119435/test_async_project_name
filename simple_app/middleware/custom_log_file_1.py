import asyncio
import threading

from asgiref.sync import sync_to_async
from django.http import HttpResponse
from django.utils.decorators import sync_and_async_middleware


# sync_only_middleware on all 3
# Asynchronous handler adapted for middleware simple_app.middleware.custom_log_3
# a = b = multi thread

# (sync_and_async_middleware | async_only_middleware) on all 3
# all middlewares using single thread
# _process_exception multi thread :(
# a = multi thread
# b = single thread


@sync_and_async_middleware
def custom_log_1(get_response):
    print('1 one time config and init')
    if asyncio.iscoroutinefunction(get_response):
        async def middleware(request):
            print('1 a before req', threading.get_ident(), asyncio.iscoroutinefunction(get_response))
            response = await get_response(request)
            print('1 a after res', threading.get_ident(), asyncio.iscoroutinefunction(get_response))
            return response

        async def _process_view(request, view_func, view_args, view_kwargs):
            print('1 a before view', threading.get_ident(), asyncio.iscoroutinefunction(view_func))

        async def _process_exception(request, exception):
            print('1 a exception', threading.get_ident(), exception)
            return HttpResponse('ex')

    else:
        def middleware(request):
            print('1 s before req', threading.get_ident(), asyncio.iscoroutinefunction(get_response))
            response = get_response(request)
            print('1 s after res', threading.get_ident(), asyncio.iscoroutinefunction(get_response))
            return response

        def _process_view(request, view_func, view_args, view_kwargs):
            print('1 s before view', threading.get_ident(), asyncio.iscoroutinefunction(view_func))

        def _process_exception(request, exception):
            print('1 s exception', threading.get_ident(), exception)
            return HttpResponse('ex')

    middleware.process_view = _process_view
    middleware.process_exception = _process_exception
    return middleware
