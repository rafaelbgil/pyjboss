from ..transport import Transport
from .datasource import DatasourcePy
from .message import MessagePy
from .ejb import EjbPy
from .utils import UtilsPy

import logging


class PyJboss(object):
    def __init__(self, controller, user, password, host=None, server=None):
        self.controller = controller
        self.user = user
        self.password = password
        self.host = host
        self.server = server

        self.transport = Transport(user=self.user,
                                   password=self.password,
                                   controller=self.controller,
                                   host=self.host,
                                   server=self.server)
        
        self.datasource = DatasourcePy(self)
        self.message = MessagePy(self)
        self.ejb = EjbPy(self)
        self.utils = UtilsPy(self)
