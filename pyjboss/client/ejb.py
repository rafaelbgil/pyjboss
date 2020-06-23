from .namespacedclient import NamespacedClient


class EjbPy(NamespacedClient):
    '''
    Class utilized to get information about ejb resources

    '''
    def list_thread_pools(self):
        payload = {"address" : [{ "subsystem" : "ejb3" }], "operation" : "read-children-names", "child-type" : "thread-pool"}
        return_data = self.transport.make_request(
            method='POST', endpoint=self.transport.controller,
            payload=payload)
        return return_data
    
    def get_thread_pool(self, thread_pool_name='default'):
        payload = {"address" : [{ "subsystem" : "ejb3" },{ "thread-pool" : thread_pool_name }], "operation" : "read-resource", "include-runtime" : True}
        
        return_data = self.transport.make_request(
            method='POST', endpoint=self.transport.controller,
            payload=payload)
        return return_data