import asyncio
import threading

from django.utils.decorators import sync_and_async_middleware, async_only_middleware, sync_only_middleware


@sync_and_async_middleware
def custom_log_2(get_response):
    print('2 one time config and init')
    if asyncio.iscoroutinefunction(get_response):
        async def middleware(request):
            print('2 a before req', threading.get_ident(), asyncio.iscoroutinefunction(get_response))
            response = await get_response(request)
            print('2 a after res', threading.get_ident(), asyncio.iscoroutinefunction(get_response))
            return response

        async def _process_view(request, view_func, view_args, view_kwargs):
            print('2 a before view', threading.get_ident(), asyncio.iscoroutinefunction(view_func))
    else:
        def middleware(request):
            print('2 s before req', threading.get_ident(), asyncio.iscoroutinefunction(get_response))
            response = get_response(request)
            print('2 s after res', threading.get_ident(), asyncio.iscoroutinefunction(get_response))
            return response

        def _process_view(request, view_func, view_args, view_kwargs):
            print('2 s before view', threading.get_ident(), asyncio.iscoroutinefunction(view_func))

    middleware.process_view = _process_view
    return middleware
