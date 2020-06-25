from .namespacedclient import NamespacedClient


class MessagePy(NamespacedClient):
    '''
    Get information about queues and topics jms
    '''

    def list(self, message_server='default', type_message='queue'):
        '''
        List a type of message queue, the type can be queue or topic

        Parameters
        ----------
        param: message_server: The message server definied in jboss/wildfly, by default the name of the message server is "default". Recommend to verify your installation.
        param: type_message: The type of message queue, this can be queue or topic, the dafult value is queue.

        Returns
        -------
        list
            Return a list with jms-queues ou jms-topics
        '''
        payload = {
            "address": [{
                "subsystem": "messaging-activemq"
            }, {
                "server": message_server
            }],
            "operation":
            "read-children-names",
            "child-type":
            "jms-" + type_message
        }
        return_data = self.transport.make_request(
            method='POST', endpoint=self.transport.controller,
            payload=payload)

        return return_data

    def get(self,
            name_resource,
            message_server='default',
            type_message='queue'):
        '''
        Get information about a queue or topic jms

        Parameters
        ----------
        param: name_resource: queue or topic name
        param: message_server: The message server definied in jboss/wildfly, by default the name of the message server is "default". Recommend to verify your installation.
        param: type_message: The type of message queue, this can be queue or topic, the dafult value is queue.

        Returns
        -------
        dictionary
            Return a dictionary with information about the queue or topic jms.
        '''
        payload = {
            "address": [{
                "subsystem": "messaging-activemq"
            }, {
                "server": message_server
            }, {
                "jms-" + type_message: name_resource
            }],
            "operation":
            "read-resource",
            "include-runtime":
            True
        }
        return_data = self.transport.make_request(
            method='POST', endpoint=self.transport.controller,
            payload=payload)

        return return_data
