# src/backend_common/exceptions/__init__.py
"""
Common exception classes for backend services.

This module provides standardized exception handling across all services.
"""

from .base import BaseError
from .business import (
    BusinessLogicError,
    NotFoundError,
    ValidationError,
    ConflictError,
    ForbiddenError,
)
from .http import (
    UnauthorizedError,
    BadRequestError,
    ServiceUnavailableError,
    TimeoutError,
)

__all__ = [
    "BaseError",
    "BusinessLogicError",
    "NotFoundError",
    "ValidationError",
    "ConflictError",
    "ForbiddenError",
    "UnauthorizedError",
    "BadRequestError",
    "ServiceUnavailableError",
    "TimeoutError",
]
