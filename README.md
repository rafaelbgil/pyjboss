# pyjboss
Client for jboss and Wildfly API written in python

This module can be used to obtain information about jboss/wildfly and its resources in a simple way for implementation, and too used by command line.

## Installation

Install the pyjboss with pip

`pip install pyjboss`

## Compatibility
* Jboss EAP >= 7
* Wildfly >= 10

## Python Compatibility
* Python >= 2.7 
* Python >= 3.0

## Example use

How to create a object and get information about jvm memory in a jboss running in `standalone mode`.

```python
>>> from pyjboss import PyJboss
>>> objboss = PyJboss(controller='ip_host_controller', user='jboss_admin_user' , password='jboss_admin_password')
>>> objboss.utils.get_memory_info()
{'heap-memory-usage': {'init': 67108864, 'used': 61638768, 'committed': 103874560, 'max': 518979584}, 'non-heap-memory-usage': {'init': 7667712, 'used': 118607784, 'committed': 134217728, 'max': 780140544}, 'object-name': 'java.lang:type=Memory', 'object-pending-finalization-count': 0, 'verbose': False}
```

How to create a object and get information about the datasource `ExampleDS` in a jboss running in `domain mode` where, there is a host in domain called `master` and the server of this host is called `server-one`

```python
>>> from pyjboss import PyJboss
>>> objboss = PyJboss(controller='ip_domain_controller', user='jboss_admin_user' , password='jboss_admin_password', host='master', server='server-one')
>>> objboss.datasource.get(datasource_type='datasource', datasource_name='ExampleDS')
{'allocation-retry': None, 'allocation-retry-wait-millis': None, 'allow-multiple-users': False, 'authentication-context': None, 'background-validation': None, 'background-validation-millis': None, 'blocking-timeout-wait-millis': None, 'capacity-decrementer-class': None, 'capacity-decrementer-properties': None, 'capacity-incrementer-class': None, 'capacity-incrementer-properties': None, 'check-valid-connection-sql': None, 'connectable': False, 'connection-listener-class': None, 'connection-listener-property': None, 'connection-url': 'jdbc:h2:mem:test;DB_CLOSE_DELAY=-1;DB_CLOSE_ON_EXIT=FALSE', 'credential-reference': None, 'datasource-class': None, 'driver-class': None, 'driver-name': 'h2', 'elytron-enabled': False, 'enabled': True, 'enlistment-trace': False, 'exception-sorter-class-name': None, 'exception-sorter-properties': None, 'flush-strategy': None, 'idle-timeout-minutes': None, 'initial-pool-size': None, 'jndi-name': 'java:jboss/datasources/ExampleDS', 'jta': True, 'max-pool-size': None, 'mcp': 'org.jboss.jca.core.connectionmanager.pool.mcp.SemaphoreConcurrentLinkedDequeManagedConnectionPool', 'min-pool-size': None, 'new-connection-sql': None, 'password': 'sa', 'pool-fair': None, 'pool-prefill': None, 'pool-use-strict-min': None, 'prepared-statements-cache-size': None, 'query-timeout': None, 'reauth-plugin-class-name': None, 'reauth-plugin-properties': None, 'security-domain': None, 'set-tx-query-timeout': False, 'share-prepared-statements': False, 'spy': False, 'stale-connection-checker-class-name': None, 'stale-connection-checker-properties': None, 'statistics-enabled': True, 'track-statements': 'NOWARN', 'tracking': False, 'transaction-isolation': None, 'url-delimiter': None, 'url-selector-strategy-class-name': None, 'use-ccm': True, 'use-fast-fail': False, 'use-java-context': True, 'use-try-lock': None, 'user-name': 'sa', 'valid-connection-checker-class-name': None, 'valid-connection-checker-properties': None, 'validate-on-match': None, 'connection-properties': None, 'statistics': {'jdbc': None, 'pool': None}}

```

### Features
This module are in the beginning of development and has the features bellow.

* Datasource: Get information about datasources and xa-datasources.
* Message: Get information about messages in a queue or a topic as well list queues or topics.
* Ejb: Get information about thread pools ejb.
* Utils: Get information about jvm memory.


