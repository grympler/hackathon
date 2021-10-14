#!/usr/bin/env python
"""Module gathering helper wrappers."""
import logging
from functools import wraps


LOGGER = logging.getLogger(__name__)


def ipdb_on_exception(fun):
    """If --ipdb is set, then launch ipdb on exception."""
    @wraps(fun)
    def wrapper(args):
        """Wraps function into ipdb exception handler."""
        if args["--ipdb"]:
            from ipdb import launch_ipdb_on_exception

            with launch_ipdb_on_exception():
                fun(args)
        else:
            try:
                result = fun(args)
            except Exception as exception:
                LOGGER.error(
                    "%s", exception, exc_info=True
                )
                raise SystemExit(1) from exception
            else:
                return result

    return wrapper


def timer(fun):
    """If --time is set, then mesure excecution time."""
    @wraps(fun)
    def wrapper(args):
        """Wraps function execution time."""
        if args["--time"]:
            import time
            start_time = time.time()
            result = fun(args)
            LOGGER.info("Total time:", time.time() - start_time)
            return result

        return fun(args)

    return wrapper
