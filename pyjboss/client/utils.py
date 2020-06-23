from .namespacedclient import NamespacedClient


class UtilsPy(NamespacedClient):
    def get_memory_info(self):
        payload = {"address": [{"core-service": "platform-mbean"}, {
            "type": "memory"}], "operation": "read-resource", "include-runtime": True}
        return_data = self.transport.make_request(
            method='POST', endpoint=self.transport.controller,
            payload=payload)
        return return_data
