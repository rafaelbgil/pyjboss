from .namespacedclient import NamespacedClient


class DeploymentPy(NamespacedClient):
    '''
    Get information about deployments and its resources
    '''

    def list(self):
        '''
        List Deployments

        Parameters
        ----------
        None

        Returns
        -------
        list
            A list of deployments like WAR or EAR packages
        '''
        payload = {"address": [], "operation": "read-children-names",
                   "child-type": "deployment"}
        return_data = self.transport.make_request(
            method='POST', endpoint=self.transport.controller,
            payload=payload)
        return return_data

    def get_undertow_information(self, deployment, sub_deployment=None):
        '''
        Get information about undertow status 

        This method is useful for get information about sessions

        Parameters
        ----------
        param: deployment: The name of package file that was deployed, the name must be with the extesion .war, .ear or .jar.
        param: sub_deployment: This parameter is optional and only be used if you have a package .ear and it has packages inside it. 
        '''
        if sub_deployment == None:
            payload = {"address": [{"deployment": deployment}, {
                "subsystem": "undertow"}], "operation": "read-resource", "include-runtime": True}
        else:
            payload = {"address": [{"deployment": deployment}, {"subdeployment": sub_deployment}, {
                "subsystem": "undertow"}], "operation": "read-resource", "include-runtime": True}

        return_data = self.transport.make_request(
            method='POST', endpoint=self.transport.controller,
            payload=payload)
        return return_data
