# coding=utf-8
# author=yphacker

import traceback


def retry(**wrap_kwargs):
    def wrapper(func):
        def _inner(*args, **kwargs):
            max_retries = wrap_kwargs.pop('max_retries', 3)
            for retries in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print('retry exception:{}'.format(traceback.format_exc()))
                    if retries + 1 >= max_retries:
                        return None

        return _inner

    return wrapper
