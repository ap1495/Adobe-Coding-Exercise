class BaseFileType:
    @abstractmethod
    def get_delimiter(self):
        pass
    
class TabDelimitedFileType(BaseFileType):
    @staticmethod
    def get_delimiter(self):
        return "\t"
    
class CommaDelimitedFileType(BaseFileType):
    @staticmethod
    def get_delimiter(self):
        return ","
    
class PipeDelimitedFileType(BaseFileType):
    @staticmethod
    def get_delimiter(self):
        return "|"