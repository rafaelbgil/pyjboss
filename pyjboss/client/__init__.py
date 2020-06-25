from ..transport import Transport
from .datasource import DatasourcePy
from .message import MessagePy
from .ejb import EjbPy
from .utils import UtilsPy

import logging


class PyJboss(object):
    '''
    Jboss Client API, provides a way to get information about jboss and Wildfly resources by its API.

    This instance has the following attributes:
        :client.datasource  This provides informations about datasources and xa-datasources
        :client.ejb         This provides informations about ejb thread pools 
        :client.messages    This provides informations about jms-queues and jms-topics
        :client.utils       This provides general informations like jvm-memory

    You can create an object for standole mode like:
        >>> objboss = PyJboss(controller='ip_host_controller', user='jboss_admin_user' , password='jboss_admin_password')
    or

    You can create an object for domain mode like:
        >>> objboss = PyJboss(controller='ip_domain_controller', user='jboss_admin_user' , password='jboss_admin_password', host='master', server='server-one')

    :param controller: IP or Hostname of jboss host controller or domain controller.
    :param user: A jboss user with administrative permissions.
    :param password: The password of jboss user.
    :param host: This parameter must be used for the domain mode only, this especify the host in domain mode that will be consulted.
    :param server: This parameter must be used for the domain mode only, this especify a server from the host that will be consulted.
    '''
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
