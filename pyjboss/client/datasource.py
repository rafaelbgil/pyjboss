from .namespacedclient import NamespacedClient


class DatasourcePy(NamespacedClient):
    ''' 
    Get information about datasources and xa-datasources

    '''

    def normalize_datasource(self, datasource_type='datasource'):
        # Method used internaly only, that is reponsible to format output from datasource and xa-datasource
        if datasource_type == 'datasource':
            datasource_type = 'data-source'
        elif datasource_type == 'xa-datasource':
            datasource_type = 'xa-data-source'
        return datasource_type

    def list(self, datasource_type='datasource'):
        '''
        Get a list of datasources by especific datasource_type

        Parameters
        ----------
        param: datasource_type: The type of datasource, that can be datasource or xa-datasource.
            if not defined "datasource" is the default value.

        Returns
        -------
        list
            A list with the datasources
        '''
        payload = {
            "address": [{
                "subsystem": "datasources"
            }],
            "operation": "read-children-names",
            "child-type": self.normalize_datasource(datasource_type)
        }

        return_data = self.transport.make_request(
            method='POST', endpoint=self.transport.controller,
            payload=payload)
        return return_data

    def get(self, datasource_name, datasource_type='datasource'):
        '''
        Get information about a datasource

        Parameters
        ----------
        param: datasource_name: The name of datasource or xa-datasoruce.
        param: datasource_type  The type of datasource can be datasource or xa-datasource
            if not defined "datasource" is the default value.

        Returns
        -------
        dictionary
            Return a dictionary with information about the datasource.
        
        For more information, can be usefull enable statistics in the datasources.
        '''
        payload = {
            "address": [{
                "subsystem": "datasources"
            }, {
                self.normalize_datasource(datasource_type):
                datasource_name
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
