import os

class HealthGuard:
    def __init__(self, lockfile_path="healthcheck.lock"):
        self.lockfile_path = lockfile_path

    def is_enabled(self) -> bool:
        return os.path.exists(self.lockfile_path)
