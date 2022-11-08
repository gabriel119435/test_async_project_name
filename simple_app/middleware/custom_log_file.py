import asyncio

from django.utils.decorators import sync_and_async_middleware, async_only_middleware, sync_only_middleware

# @async_only_middleware
# a = async mw | multi thread
# b = async mw | single thread

# @sync_only_middleware
# Asynchronous handler adapted for middleware simple_app.middleware.custom_log.
# a = sync mw | multi thread
# b = sync mw | multi thread

# @sync_and_async_middleware
# a = async mw | multi thread
# b = async mw | single thread


@sync_and_async_middleware
def custom_log(get_response):
    print('one time config and init')
    if asyncio.iscoroutinefunction(get_response):
        async def middleware(request):
            print('a - before req')
            response = await get_response(request)
            print('a - after res')
            return response

    else:
        def middleware(request):
            print('before req')
            response = get_response(request)
            print('after res')
            return response
    middleware.process_view = custom_process_view
    return middleware


def custom_process_view(request, view_func, view_args, view_kwargs):
    print('before view')
