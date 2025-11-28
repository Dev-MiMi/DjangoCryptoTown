import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "crypto_town.users"
    verbose_name = _("Users")

    def ready(self):
        with contextlib.suppress(ImportError):
            import crypto_town.users.signals  # noqa: F401, PLC0415
