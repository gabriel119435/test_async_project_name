import asyncio
from functools import wraps, partial


def to_async():
    def inner(func):
        @wraps(func)
        async def run(*args, **kwargs):
            return await asyncio.get_event_loop().run_in_executor(executor=None, func=partial(func, *args, **kwargs))

        return run

    return inner
