"""Logging module of PyVyuham"""

import logging

__author__ = 'Kenash K'

class vyLogger(object):
    '''vyLogger class
    '''
    
    def __init__(self, logname, loglevel=logging.DEBUG, logfile='pyvyuham_master_log', defaultlogloc='./logs'):
        self.logpath = os.path.join(defaultlogloc,logfile)
        self.logger = logging.getLogger(logname)
        self.logger.setLevel(loglevel)
        
        #pyVyuham Master log
        self.loghandler = logging.FileHandler(self.logpath)
        loghandler.setLevel(loglevel)
        
        #pyVyuham Logging format
        self.logformat = logging.Formatter('%(asctime)s : %(name)s : %(levelname)s : %(message)s')
        self.loghandler.setFormatter(self.logformat)
        
        #pyVyuham log handlers
        self.logger.addHandler(handler)
        
        
               