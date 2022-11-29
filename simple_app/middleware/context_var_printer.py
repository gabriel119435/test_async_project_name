from contextvars import copy_context, Context


def print_context():
    ctx: Context = copy_context()
    print(list(ctx.items()))
