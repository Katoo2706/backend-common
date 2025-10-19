# src/backend_common/auth/__init__.py
"""
Authentication and authorization utilities for backend services.

Provides JWT-based authentication, service-to-service auth,
and FastAPI dependencies for securing endpoints.
"""

from .manager import AuthManager, JWTAuthManager
from .dependencies import require_auth, require_service_auth, get_current_user

__all__ = [
    "AuthManager",
    "JWTAuthManager",
    "require_auth",
    "require_service_auth",
    "get_current_user",
]
