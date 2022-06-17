try:
    from ._version import version as __version__
except ImportError:
    __version__ = "unknown"

from ._line import DraggableLine

__author__ = "Ian Hunt-Isaak"
__email__ = "ianhuntisaak@gmail.com"

__all__ = [
    "__version__",
    "__author__",
    "__email__",
    "DraggableLine",
]
