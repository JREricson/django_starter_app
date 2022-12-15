import logging

from django.core.management import call_command

django_logger = logging.getLogger("django")


def backup_db_job():
    try:
        call_command("dbbackup")
    except Exception:
        django_logger.error(f"Problem with backup. {Exception.with_traceback}")
