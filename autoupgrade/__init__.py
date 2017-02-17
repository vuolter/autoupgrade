# -*- coding: utf-8 -*-

from .exceptions import NoVersionsError, PIPError, PkgNotFoundError
from .package import Package
from .utils import normalize_version


# NOTE: Legacy class
class AutoUpgrade(Package):

    def upgrade(self, *args, **kwargs):
        try:
            Package.upgrade(self, *args, **kwargs)
        except PIPError:
            return False
        else:
            return True
