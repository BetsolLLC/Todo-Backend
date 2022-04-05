import logging


def custom_logger(logger):
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler = logging.FileHandler('stattic.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger
