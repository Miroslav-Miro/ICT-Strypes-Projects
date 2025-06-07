class OldLogger:
    def write_log(self, message):
        print(f"[OLD LOG]: {message}")


def process(logger):
    logger.log("Something happened")


class LoggerAdapter:
    def __init__(self, old_logger):
        self.old_logger = old_logger

    def log(self, message):
        self.old_logger.write_log(message)


old_logger = OldLogger()
adapter = LoggerAdapter(old_logger)
process(adapter)
