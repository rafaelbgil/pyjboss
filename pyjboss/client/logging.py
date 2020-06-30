from .namespacedclient import NamespacedClient


class LoggingPy(NamespacedClient):
    '''
    Get information about logs files
    '''

    def list(self):
        '''
        Get a list of log files

        Parameters
        ----------
        None

        Returns
        -------
        list
            A list with log files and information of then
        '''
        payload = {"address": [{"subsystem": "logging"}],
                   "operation": "list-log-files"}
        return self.transport.make_request(
            method='POST', endpoint=self.transport.controller,
            payload=payload)

    def read_log(self, filename='server.log', lines=10, tail=False):
        '''
        Read a log file

        Parameters
        ----------
        param: filename: Log file name
        param: lines: Amount of lines read
        param: If true, the read will be done by end of log file
        
        Returns
        -------
        Array
            A array with a line per position
        '''
        payload = {"address" : [{ "subsystem" : "logging" },{ "log-file" : filename }], "operation" : "read-log-file", "tail" : tail, "lines" : lines}
        return self.transport.make_request(
            method='POST', endpoint=self.transport.controller,
            payload=payload)