#Main object class for the Framework
import vylogger

import vyUtils.vymarshal as vymarshal
import vyUtils.vyscout as vyscout

class vyMain:
    def __init__(self):
        """Build PyVyuham
        """
        self.scout=vyscout()
        self.marshal=vymarshal()