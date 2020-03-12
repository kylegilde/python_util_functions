# !/usr/bin/env/python3


def get_object_name(obj):
    """
    Get the name of a variable in the calling namespace as a string

    Parameters
    ----------
    obj: any variable

    Returns
    -------
    a string
    
    """
    import inspect
    namespace = dict(globals(), **locals()) # inspect.stack()[1][0].f_globals
    return [name for name in namespace if namespace[name] is obj][0]


