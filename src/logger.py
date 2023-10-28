import json

from datetime import datetime
from config import config


def logger(func):
    def wrapper(*args, **kwargs):
        start_t = datetime.now()
        
        result = func(*args, **kwargs)
    
        end_t = datetime.now()

        with open(config['logs_path'], mode='r+', encoding='utf-8') as file:
            entry = {
                'name': func.__name__,
                'args': [repr(arg) for arg in args],
                'kwargs': [repr(kwarg) for kwarg in kwargs],
                'time': str(end_t - start_t),
                'result': result
            }
            log = json.load(file)
            log.append(entry)
            file.seek(0)
            json.dump(log, file, indent=4)
        
        return result
    
    return wrapper
