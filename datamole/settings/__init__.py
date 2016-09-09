from debug_conf import debug


if (debug is True):
    from development import *
else:
    from production import *
