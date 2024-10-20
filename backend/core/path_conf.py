import os

from pathlib import Path

BasePath = Path(__file__).resolve().parent.parent

# alembic path
ALEMBIC_Versions_DIR = os.path.join(BasePath, "alembic", "versions")

# log path
LOG_DIR = os.path.join(BasePath, "log")
