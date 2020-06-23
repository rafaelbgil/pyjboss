from .namespacedclient import NamespacedClient


class MessagePy(NamespacedClient):
    def list(self, message_server='default', type_message='queue'):
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
