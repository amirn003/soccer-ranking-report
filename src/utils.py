#! /usr/bin/env python3
# coding: utf8

from progressbar import ProgressBar
import logging
import datetime
import shutil
import click
import os
from logging.handlers import RotatingFileHandler


def set_progress_bar(list_in_for: list) -> ProgressBar:
    """For progressbar with list
-
    Args:
        List for getting length

    Returns:
        ProgressBar

    """
    try:

        progress_bar = ProgressBar(max_value=len(list_in_for),
                                   redirect_stdout=True)
        return progress_bar

    except Exception as e:
        print("omf.set_progress_bar ERROR : {}".format(e))


def set_progress_bar_number(number: int) -> ProgressBar:
    """For progressbar with number

    Args:
        number: Length

    Returns:
        ProgressBar

    """
    try:

        progress_bar = ProgressBar(max_value=number,
                                   redirect_stdout=True)
        return progress_bar

    except Exception as e:
        print("omf.set_progress_bar_number ERROR : {}".format(e))


def update_progress_bar(bar: ProgressBar, indice: int) -> int:
    """Change Update bar progression

    Args:
        bar: Progress Bar using
        indice: Indice

    Returns:
        indice+1

    """
    try:

        bar.update(indice)
        indice += 1
        return indice

    except Exception as e:
        print("omf.update_progress_bar ERROR : {}".format(e))


def finish_progress_bar(bar: ProgressBar):
    """Close progress Bar

    Args:
        bar: Progress Bar using

    """
    try:

        bar.finish()

        print("\n")

    except Exception as e:
        print("omf.finish_progress_bar ERROR : {}".format(e))



def set_logger(terminal_level, file_level, directory: str, log_name: str = '', mode: chr = 'a') -> None:
    """Set logger levels to be printed in terminal and in log file

    Args:
        terminal_level: str (debug info error) or int (10, 20, 30) - log level of info to print in terminal
        file_level: str (debug info error) or int (10, 20, 30) - log level of info to print in log file
        directory: log directory to be created
        log_name: prefix of log name
        mode: logging.hadelers mode

    """

    # Set prints attributes of the logging module
    logger = logging.getLogger('log')
    logger.setLevel(logging.DEBUG)

    # One hangler toward the console
    ch = logging.StreamHandler()

    # Define logging level to be printed in the console

    ch.setLevel(eval_level(terminal_level))

    # directory = os.getcwd()
    # Create dir in which to put the logs if it doesn't already exist
    directory = create_dir(directory)
    # One handler toward a log file
    if not log_name:
        log_name = "log_file_" + str(datetime.datetime.now().date())
    log_file_name = os.path.join(directory, "{}.log".format(log_name))
    fh = logging.handlers.RotatingFileHandler(filename=log_file_name, mode=mode, maxBytes=1000000000, backupCount=100)
    fh.setLevel(eval_level(file_level))

    formatter = logging.Formatter('%(asctime)s %(process)s %(name)-12s %(levelname)-8s %(message)s')
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)


def create_dir(directory: str, delete: bool = False) -> str:
    """Create a folder if it doesn't exist

    Args:
        directory: directory to be created
        delete: should we delete the directory if it already exist

    Returns:
        directory

    """
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)

        elif delete and click.confirm('Are you sure you want to DELETE directory {} '.format(directory, default=False)):
            # If dir already exists, then delete it with its content and recreate it
            shutil.rmtree(directory)
            os.makedirs(directory)
        return directory

    except Exception as e:
        print('')

def eval_level(level) -> int:
    """Define logging level to be printed

    Args:
        level: log level to eval

    Returns:
        the logging.mode

    """

    if level == "debug" or level == 10:
        return logging.DEBUG

    elif level == "info" or level == 20:
        return logging.INFO

    elif level == "warning" or level == 30:
        return logging.WARNING

    elif level == "error" or level == 40:
        return logging.ERROR
    else:
        return logging.ERROR
