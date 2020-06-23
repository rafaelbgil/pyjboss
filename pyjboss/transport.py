import requests
import json

class Transport(object):
    '''
    Class used to make requests to jboss api and manage errors
    '''

    def __init__(self, user, password, controller, host=None, server=None):
        self.user = user
        self.password = password
        self.controller = "http://" + controller + ":9990/management"
        self.host = host
        self.server = server
    
    def analise_return(self, request):
        if request.status_code ==  401:
            print("user or password invalid.")
            return False
        elif not 'result' in request.json():
            print("No resources found.")
            return False
        elif request.ok and len(request.json()['result']) > 0:
            return request.json()['result']
        elif len(request.json()['result']) == 0:
            print("No resources found.")
            return False
        

    def make_request(self, method, endpoint, payload=None, params=None):
        headers = {'content-type': 'application/json'}
        authentication = requests.auth.HTTPDigestAuth(
            username=self.user, password=self.password)
        if payload is not None:
            if not self.server == None:
                payload['address'].insert(0, {"server" : self.server})
            if not self.host == None:
                payload['address'].insert(0, {"host" : self.host})
            payload = json.dumps(payload)
        if method == 'POST':
            try:
                return self.analise_return(requests.post(auth=authentication, url=endpoint, headers=headers, data=payload))
            except requests.exceptions.ConnectionError:
                print("Cannot connect to host controller url %s." % (self.controller))
                return False
            except: 
                print("Cannot obtain a valid reponse.")
                return False
        
