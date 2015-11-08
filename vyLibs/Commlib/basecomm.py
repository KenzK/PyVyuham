


class BaseComm:
    """This is base class for the communication library
    """
    def __init__(self, hostname='', port='', auth='', password=''):
        """
        Base Communication library init
        """
        self.host = hostname
        self.port = port
        self.auth = auth
        self.password = password

    def connect(self):
        """
        Connect to the device
        """
        pass

    def send_command(self):
        """Send the command string
        """
        pass

    def get_response(self):
        """return the response of command
        """
        pass


