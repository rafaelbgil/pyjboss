import unittest
from pyjboss import PyJboss
from sys import argv


class TestStandalone(unittest.TestCase):
    '''
    Tests executed on jboss in standalone mode
    '''

    def setUp(self):
        self.controller = ''
        self.jboss_user = ''
        self.jboss_password = ''
        self.objboss = PyJboss(controller=self.controller,
                               user=self.jboss_user, password=self.jboss_password)

    # Test for ejb resources and features

    def testListThreadPools(self):
        self.assertIn('default', self.objboss.ejb.list_thread_pools())

    def testGetThreadPool(self):
        return_thread_pool = self.objboss.ejb.get_thread_pool('default')
        self.assertIn('name', return_thread_pool,
                      "Thread pool %s not found." % ('default'))

    # Test for datasource resources and features
    def testListDatasources(self):
        self.assertIn('ExampleDS', self.objboss.datasource.list(
            datasource_type='datasource'))

    def testGetDatasource(self):
        return_datasource = self.objboss.datasource.get(
            datasource_name='ExampleDS', datasource_type='datasource')
        self.assertIn('enabled', return_datasource,
                      "Datasource %s not found." % ('ExampleDS'))

    # Test for message resources and features
    def testListQueues(self):
        self.assertIn('DLQ', self.objboss.message.list(
            message_server='default', type_message='queue'))

    def testGetQueue(self):
        return_queue = self.objboss.message.get(
            type_message='queue', name_resource='DLQ', message_server='default')
        self.assertIn('dead-letter-address', return_queue, msg='Queue or topic jms not found.')
    
    # Test for utils features
    def testGetMemory(self):
        self.assertIn('heap-memory-usage',self.objboss.utils.get_memory_info())


if __name__ == '__main__':
    unittest.main()
