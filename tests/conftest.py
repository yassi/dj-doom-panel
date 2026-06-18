"""
Pytest configuration for dj-doom-panel tests.
"""

import os
import sys
import django
from django.conf import settings


def pytest_configure(config):
    """Configure Django for pytest."""
    example_project_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), "example_project"
    )
    if example_project_path not in sys.path:
        sys.path.insert(0, example_project_path)

    test_db_backend = os.environ.get("TEST_DB_BACKEND", "sqlite").lower()

    if test_db_backend == "postgresql":
        os.environ.setdefault("DB_ENGINE", "postgresql")
        os.environ.setdefault("POSTGRES_HOST", "localhost")
        os.environ.setdefault("POSTGRES_PORT", "5432")
        os.environ.setdefault("POSTGRES_USER", "postgres")
        os.environ.setdefault("POSTGRES_PASSWORD", "postgres")
        os.environ.setdefault("POSTGRES_DB", "postgres")
    else:
        os.environ.setdefault("DB_ENGINE", "sqlite")

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "example_project.settings")

    if not settings.configured:
        django.setup()
