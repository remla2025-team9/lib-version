try:
    from importlib.metadata import version, PackageNotFoundError
except ImportError:
    from importlib_metadata import version, PackageNotFoundError

from . import version as local_version

class VersionUtil:
    @staticmethod
    def get_version():
        try:
            return version("lib-version")
        except PackageNotFoundError:
            return local_version.__version__
