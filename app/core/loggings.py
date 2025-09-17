import logging
import sys


class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        return (
            '{"level": "%(levelname)s", "ts": "%(asctime)s", '
            '"logger": "%(name)s", "msg": "%(message)s"}'
        ) % record.__dict__


def setup_logging() -> None:
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(JsonFormatter("%(asctime)s"))
    root = logging.getLogger()
    root.setLevel(logging.INFO)
    root.handlers = [handler]