from abc import abstractmethod
from app_enums import TAB_FILE_DELIMITER, COMMA_FILE_DELIMITER, PIPE_FILE_DELIMITER

class BaseFileType:
    def __init__(self):
        pass
    
    @classmethod
    def initialize_file_type_obj(cls, delimiter):
        if delimiter == TAB_FILE_DELIMITER:
            file_type_obj = TabDelimitedFileType()
            
        elif delimiter == COMMA_FILE_DELIMITER:
            file_type_obj = CommaDelimitedFileType()
            
        elif delimiter == PIPE_FILE_DELIMITER:
            file_type_obj = PipeDelimitedFileType()
            
        return file_type_obj
    
    @abstractmethod
    def get_delimiter(self):
        pass
    
class TabDelimitedFileType(BaseFileType):
    def __init__(self):
        super().__init__()
    
    def get_delimiter(self):
        return TAB_FILE_DELIMITER
    
class CommaDelimitedFileType(BaseFileType):
    def __init__(self):
        super().__init__()
        
    def get_delimiter(self):
        return COMMA_FILE_DELIMITER
    
class PipeDelimitedFileType(BaseFileType):
    def __init__(self):
        super().__init__()
        
    def get_delimiter(self):
        return PIPE_FILE_DELIMITER