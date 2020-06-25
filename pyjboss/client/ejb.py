from .namespacedclient import NamespacedClient


class EjbPy(NamespacedClient):
    '''
    Get informations about ejb resources

    '''
    def list_thread_pools(self):
        '''
        List thread pools

        Parameters
        ----------
        None

        Returns
        -------
        list
            A list of thread pools
        '''
        payload = {"address" : [{ "subsystem" : "ejb3" }], "operation" : "read-children-names", "child-type" : "thread-pool"}
        return_data = self.transport.make_request(
            method='POST', endpoint=self.transport.controller,
            payload=payload)
        return return_data
    
    def get_thread_pool(self, thread_pool_name='default'):
        ''' 
        Get information about a thread pool

        Parameters
        ----------
        param: thread_pool_name: The thread pool that desired get information.
            if not defined "default" is the default value.

        Returns
        -------
        dictionary
            Return a dictionary with information about the thread pool.
        '''
        payload = {"address" : [{ "subsystem" : "ejb3" },{ "thread-pool" : thread_pool_name }], "operation" : "read-resource", "include-runtime" : True}
        
        return_data = self.transport.make_request(
            method='POST', endpoint=self.transport.controller,
            payload=payload)
        return return_data