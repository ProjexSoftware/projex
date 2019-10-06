""" 
Defines the build setup errors.
"""


class XBuildError(Exception):
    pass


# I
# ---------------------------------------------------------------------


class InvalidBuildPath(XBuildError):
    def __init__(self, buildpath):
        msg = '{0} is not a valid build path'.format(buildpath)
        XBuildError.__init__(self, msg)
