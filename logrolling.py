"""An encapsulation of logging to make using it easier and more pythonic
"""


import logging


class IndentLogFormatter(logging.Formatter):
    """Formatter to be used with logging that puts message in lines following
    the log metainformation, indented.
    """
    def format(self, record):
        out_str = super().format(record)
        out_str = out_str.replace("\n", "\n    ")
        return out_str


class LogWrapper:
    """Keeps track of details of logging
    """
    def __init__(self, logger_name, logged_modules, use_console=True):
        """
        Args:
            logger_name (str):
            logged_modules (list):
            use_console (bool):
        """
        self.logger = None
        self.filehandles = {}
        self.logged_modules = logged_modules

        # create logger
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.DEBUG)

        # add logging of requested imports
        for logger_name in self.logged_modules:
            logging.getLogger(logger_name).setLevel(logging.DEBUG)

        if use_console:
            self.add_consolehandler()

    def get_logger(self):
        return self.logger

    def add_consolehandler(self):
        # console handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        self.logger.addHandler(ch)

        # add logging of requested imports
        for logger_name in self.logged_modules:
            logging.getLogger(logger_name).addHandler(ch)

    def add_filehandler(self, logfile_path):
        # make to string for python 3.5 logging and dict key
        logfile_path = str(logfile_path)

        # log file handler
        fh = logging.FileHandler(logfile_path, mode='w')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(
                IndentLogFormatter(
                    '%(asctime)s - %(name)s - %(levelname)s\n%(message)s'
                    )
                )
        self.logger.addHandler(fh)

        # add logging of requested imports
        for logger_name in self.logged_modules:
            logging.getLogger(logger_name).addHandler(fh)

        self.filehandles[logfile_path] = fh

        return fh

    def remove_filehandler(self, logfile_path):
        self.logger.removeHandler(self.filehandles[str(logfile_path)])

    # convenience functions to pass through to logger
    def debug(self, *args, **kwargs):
        self.logger.debug(*args, **kwargs)
    def info(self, *args, **kwargs):
        self.logger.info(*args, **kwargs)
    def warning(self, *args, **kwargs):
        self.logger.warning(*args, **kwargs)
    def error(self, *args, **kwargs):
        self.logger.error(*args, **kwargs)

