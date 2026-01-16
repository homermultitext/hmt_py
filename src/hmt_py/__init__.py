from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("hmt_py") # 'name' of package from pyproject.toml
except PackageNotFoundError:
    # Package is not installed (e.g., running from a local script)
    __version__ = "unknown"

from .archive import HmtArchive

__all__ = ["HmtArchive"]