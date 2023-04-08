import sys
import logger
import logging

def error_detail_message(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error ocurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        filename,exc_tb.tb_lineno,str(error))

    return error_message

    

class customException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_detail_message(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
    
if __name__=="__main__":
    try:
        a = 1/0
    
    except Exception as e:
        logging.info("Invalid Expression")
        raise customException(e,sys)