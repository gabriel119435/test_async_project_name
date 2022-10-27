import asyncio
from functools import wraps


# https://code.djangoproject.com/ticket/31949

def both_csrf_exempt(view_func):
    def wrapped_view(*args, **kwargs):
        return view_func(*args, **kwargs)

    async def a_wrapped_view(*args, **kwargs):
        return await view_func(*args, **kwargs)

    wrapped_view.csrf_exempt = True
    a_wrapped_view.csrf_exempt = True
    return wraps(view_func)(a_wrapped_view if asyncio.iscoroutinefunction(view_func) else wrapped_view)
