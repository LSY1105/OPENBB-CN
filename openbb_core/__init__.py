"""
OPENBB-CN Core Package
面向中国市场的开源金融数据平台核心模块
"""

__version__ = "0.1.0"
__author__ = "OPENBB-CN Team"

from openbb_core.core import OpenBB
from openbb_core.router import Router

__all__ = ["OpenBB", "Router", "__version__"]
