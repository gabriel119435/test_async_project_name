import asyncio
import threading
from contextvars import ContextVar

from django.utils.decorators import sync_and_async_middleware

from simple_app.middleware.context_var_printer import print_context
from simple_app.services.s_svc import create_random_string

var = ContextVar('variable_name_3', default='default_3')


@sync_and_async_middleware
def custom_log_3(get_response):
    print(var.get(), '3 one time config and init')
    if asyncio.iscoroutinefunction(get_response):
        async def middleware(request):
            var.set('async_3' + create_random_string())
            print(var.get(), '3 a before req', threading.get_ident(), asyncio.iscoroutinefunction(get_response))
            print_context()
            response = await get_response(request)
            print(var.get(), '3 a after res', threading.get_ident(), asyncio.iscoroutinefunction(get_response))
            return response

        async def _process_view(request, view_func, view_args, view_kwargs):
            print(var.get(), '3 a before view', threading.get_ident(), asyncio.iscoroutinefunction(view_func))
    else:
        def middleware(request):
            var.set('sync_3' + create_random_string())
            print(var.get(), '3 s before req', threading.get_ident(), asyncio.iscoroutinefunction(get_response))
            response = get_response(request)
            print(var.get(), '3 s after res', threading.get_ident(), asyncio.iscoroutinefunction(get_response))
            return response

        def _process_view(request, view_func, view_args, view_kwargs):
            print(var.get(), '3 s before view', threading.get_ident(), asyncio.iscoroutinefunction(view_func))

    middleware.process_view = _process_view
    return middleware
