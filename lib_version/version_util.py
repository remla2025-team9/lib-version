"""
Version utility module for retrieving the current version of lib-version.

This module provides a centralized way to get the version, falling back to
package metadata if the local version file is unavailable.
"""

from lib_version.__version__ import version as local_version

class VersionUtil:
    """Utility class for retrieving the library version."""
    
    @staticmethod
    def get_version():
        """
        Get the current version of lib_version.
        
        Returns:
            str: The version string (e.g., "v1.0.1" or "v1.0.1-pre-1")
            
        Notes:
            First attempts to get version from local __version__.py file.
            Falls back to installed package metadata if local file unavailable.
        """
        try:
            # Try to get version from local version file first
            return local_version
        except (AttributeError, ImportError):
            # Fall back to installed package metadata
            try:
                import importlib.metadata
                version = importlib.metadata.version("lib_version")
                return f"v{version}"
            except:
                return "NOT_SET"


if __name__ == "__main__":
    print(f"lib-version: {VersionUtil.get_version()}")
