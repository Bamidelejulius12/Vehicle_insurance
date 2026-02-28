import sys
import logging

def error_message_detail(error: Exception, error_detail:sys) -> str:
    """"
    Extract detailed error information including file name, line number, and the error message
    :param error: the exeception that occurred
    :param error_detail: the sys module to access traceback deatils
    :return: A formatted error message string
    """
    # Extract traceback deatils (exception information)
    _, _, exc_tb = error_detail.exc_info()

    # get the file name where the exception occurred
    file_name = exc_tb.tb_frame.f_code.co_filename

    # Create a formatted error message string with file name, line number, and the actual error
    line_number = exc_tb.tb_lineno 
    error_message= f"Error occurred in python script: [{file_name}] at line number [{line_number}]: {str(error)}"

    # Log the error for better tracking
    logging.error(error_message)

    return error_message


class MyException(Exception):
    """
    Custom exeception class for handling error in the US visa application.
    """
    def __init__(self, error_message: str, error_detail: sys):
        """
        initialize the USVisaException with a detailed exception error message
        :param error_message: A string describing the error
        :param error_detail: The sys module to access traceback details.
        # call the base class constructor with the error message
        """
        # call the base class constructor with error message
        super().__init__(error_message)

        # format the detailed error message using error_message detail function
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self) -> str:
        """
        Return the string representation of the error message.
        """
        return self.error_message


