from .namespacedclient import NamespacedClient


class UtilsPy(NamespacedClient):
    '''
    General information that is not provided by a especific jboss subsystem will be here, like jvm memory information.
    '''
    def get_memory_info(self):
        '''
        Get memory about jvm memory

        Parameters
        ----------
        None

        Returns
        -------
        dictionary
            Return a dictionary with information about jvm memory, java heap space, non-heap space and others.
        '''
        payload = {"address": [{"core-service": "platform-mbean"}, {
            "type": "memory"}], "operation": "read-resource", "include-runtime": True}
        return_data = self.transport.make_request(
            method='POST', endpoint=self.transport.controller,
            payload=payload)
        return return_data
