# -*- coding: utf-8 -*-


class NoVersionsError(Exception):
    """
    No versions found for package.
    """

    def __str__(self):
        return """<NoVersionsError {}>""".format(self.message)


class PIPError(Exception):
    """
    PIP process failure.
    """

    def __str__(self):
        return """<PIPError {}>""".format(self.message)


class PkgNotFoundError(Exception):
    """
    No package found.
    """

    def __str__(self):
        return """<PkgNotFoundError {}>""".format(self.message)
