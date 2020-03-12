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
    namespace = inspect.stack()[1][0].f_globals
    return [name for name in namespace if namespace[name] is obj][0]


def print_shape(x, return_shape=False):
    """
    Print the variable name and shape

    Parameters
    ----------
    x: any variable with the attribute "shape"
    return_shape: if True, returns the shape tuple, default is False

    Returns
    -------
    Prints the object name and shape
    Only returns the shape if return_shape=True
    
    """
    assert hasattr(x, 'shape'), 'Object does not have shape attribute'
    
    x_name = get_object_name(x)
    print(x_name, x.shape)
    
    if return_shape:
        return x.shape
