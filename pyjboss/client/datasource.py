from .namespacedclient import NamespacedClient


class DatasourcePy(NamespacedClient):
    ''' 
    Class used to management the datasources

    '''
    def normalize_datasource(self, datasource_type='datasource'):
        #Method utilized internaly only, that is reponsible to format output from datasource and xa-datasource
        if datasource_type == 'datasource':
            datasource_type = 'data-source'
        elif datasource_type == 'xa-datasource':
            datasource_type = 'xa-data-source'
        return datasource_type

    def list(self, datasource_type='datasource'):
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

    def get(self, datasource_type, datasource_name):
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
