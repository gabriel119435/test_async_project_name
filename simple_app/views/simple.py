import asyncio
import threading
import time
from datetime import datetime
from random import random, getrandbits

from django.http import HttpResponse


def a(request):
    print('a', threading.get_ident(), asyncio.iscoroutinefunction(a))
    time.sleep(10)
    # raise ValueError('bug')
    return HttpResponse("hi")


async def b(request):
    print('b', threading.get_ident(), asyncio.iscoroutinefunction(b))
    await asyncio.sleep(10)
    # raise ValueError('bug')
    return HttpResponse("hi")


async def as_wait(t):
    await asyncio.sleep(t)
    return random()


async def c(request):
    print('c', threading.get_ident(), asyncio.iscoroutinefunction(c))
    print(datetime.now().second)
    r0 = await as_wait(2)
    r1 = await as_wait(2)
    r2 = await as_wait(2)
    r3 = await as_wait(2)
    r4 = await as_wait(2)
    print(r0, r1, r2, r3, r4)
    print(datetime.now().second)
    return HttpResponse("hi")


async def d(request):
    print('d', threading.get_ident(), asyncio.iscoroutinefunction(c))
    print(datetime.now().second)
    r0, r1, r2, r3, r4 = await asyncio.gather(
        as_wait(2),
        as_wait(2),
        as_wait(2),
        as_wait(2),
        as_wait(2)
    )
    print(r0, r1, r2, r3, r4)
    print(datetime.now().second)
    return HttpResponse("hi")


async def _raise(t):
    await asyncio.sleep(t)
    if bool(getrandbits(1)):
        raise ValueError('bug')
    return t


async def bad(request):
    print('d', threading.get_ident(), asyncio.iscoroutinefunction(c))
    print(datetime.now().second)
    r0, r1, r2, r3, r4 = await asyncio.gather(
        _raise(2),
        _raise(2),
        _raise(2),
        _raise(2),
        _raise(2),
        return_exceptions=True
    )
    print(type(r0), type(r1), type(r2), type(r3), type(r4))
    print(r0, r1, r2, r3, r4)
    print(datetime.now().second)
    return HttpResponse("hi")
