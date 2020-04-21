import logging


def get_formatter(format: str = "[{asctime}] [{levelname:<6}] {name}: {message}",
                  date_format: str = "%Y-%m-%d %H:%M:%S",
                  style: str = "{") -> logging.Formatter:
    return logging.Formatter(
        fmt=format,
        datefmt=date_format,
        style=style)


def get_file_handler(log_file_name: str,
                     formatter: logging.Formatter,
                     mode: str = 'a',
                     encoding: str = 'utf-8') -> logging.FileHandler:
    file_handler: logging.FileHandler = logging.FileHandler(
        filename=log_file_name,
        mode=mode,
        encoding=encoding)

    file_handler.setFormatter(formatter)

    return file_handler


def get_logger(log_file_name: str,
               level: int = logging.INFO) -> logging.Logger:
    formatter: logging.Formatter = get_formatter()

    fileHandler: logging.FileHandler = get_file_handler(log_file_name=log_file_name,
                                                        formatter=formatter)

    logger: logging.Logger = logging.getLogger(log_file_name)

    logger.addHandler(fileHandler)

    logger.setLevel(level)

    return logger
