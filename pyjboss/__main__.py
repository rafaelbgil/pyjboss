from __future__ import absolute_import
import json
import argparse

# Metodo responsible for format output to user


def print_pretty(command_return):
    transform_json = json.dumps(command_return, indent=2)
    print(transform_json)


class main():
    from . import PyJboss

    # main command
    description = 'This package can be used to call the jbossapi by http protocol and return values'
    main_parse = argparse.ArgumentParser(prog='jbosspy',
                                         description=description)

    main_parse.add_argument('-u', '--user',
                            help="Jboss user with administrator permissions.")
    main_parse.add_argument('-p', '--password',
                            help="Jboss user password.")
    main_parse.add_argument('-c', '--controller',
                            help="IP or name of Jboss host controller, or domain controller.")
    main_parse.add_argument('--host',
                            help="A host from domain. This option is only necessary if your jboss is running in domain mode.")
    main_parse.add_argument('--server',
                            help="A server from the host. This option is only necessary if your jboss is running in domain mode.")
    main_parse.add_argument("-v",
                            "--verbose",
                            action="store_true",
                            required=False)

    main_subparse = main_parse.add_subparsers(title="Commands", dest='command')
    main_subparse.required = True

    # parse ejb command
    ejb_parse = main_subparse.add_parser(name="ejb",
                                         help='Manage ejb resources',
                                         description="Call the ejb resources")
    ejb_parse.add_argument(
        '--list-thread-pools', help="Return a list of thread pools", action="store_true")
    ejb_parse.add_argument("--get-thread-pool",
                           help="Get information about an thread pool")
    ejb_parse.set_defaults(command="ejb")

    # parse message command
    message_parse = main_subparse.add_parser(
        name="message",
        help="Manage message resources",
        description="Call the message ressources")
    message_parse.add_argument('--queue-name', help="Queue name")
    message_parse.add_argument('--topic-name', help="Topic name")
    message_parse.add_argument('--list',
                               choices=['queue', 'topic'],
                               help="Return a list of queues or topics")
    message_parse.add_argument(
        '--message-server',
        required=True,
        help="Name of the server defined in the message resource")
    message_parse.set_defaults(command="message")

    # parse datasource command
    datasource_parse = main_subparse.add_parser(
        name="datasource",
        help="Manage datasource resources",
        description="Get information about datasources")
    datasource_parse.add_argument(
        '--datasource',
        help="Show information about an datasource, important: to obtain more information enable datasource statistic"
    )
    datasource_parse.add_argument(
        '--xa-datasource',
        help="Return information about an xa-datasource, important: to obtain more information enable datasource statistic"
    )
    datasource_parse.add_argument('--list',
                                  help="Obtain a list of datasources", choices=['datasource', 'xa-datasource'])
    datasource_parse.set_defaults(command="datasource")

    # parse utils command
    utils_parse = main_subparse.add_parser(
        name='utils',
        help='Get information aboute many resources in general'
    )
    utils_parse.add_argument('--get-memory-info',
                             help='Get jvm memory in use',
                             action="store_true",
                             required=False
                             )
    utils_parse.set_defaults(command="utils")

    # return main_parse
    parse_return = main_parse.parse_args()

    # create a PyJboss object
    obJboss = PyJboss(controller=parse_return.controller,
                      user=parse_return.user,
                      password=parse_return.password,
                      host=parse_return.host,
                      server=parse_return.server)

    # process command ejb
    if parse_return.command == 'ejb':
        if parse_return.list_thread_pools:
            print_pretty(command_return=obJboss.ejb.list_thread_pools())
        else:
            print_pretty(command_return=obJboss.ejb.get_thread_pool(
                thread_pool_name=parse_return.get_thread_pool))

    # process command message
    elif parse_return.command == 'message':
        if parse_return.list == 'queue':
            print_pretty(obJboss.message.list(
                message_server=parse_return.message_server, type_message='queue'))
        elif parse_return.list == 'topic':
            print_pretty(obJboss.message.list(
                message_server=parse_return.message_server, type_message='topic'))
        elif parse_return.queue_name:
            print_pretty(
                obJboss.message.get(name_resource=parse_return.queue_name,
                                    message_server=parse_return.message_server,
                                    type_message="queue"))

        elif parse_return.topic_name:
            print_pretty(
                obJboss.message.get(name_resource=parse_return.topic_name,
                                    message_server=parse_return.message_server,
                                    type_message="topic"))
    # process command datasource
    elif parse_return.command == 'datasource':
        if parse_return.list:
            print_pretty(obJboss.datasource.list(
                datasource_type=parse_return.list))
        elif parse_return.datasource:
            print_pretty(
                obJboss.datasource.get(
                    datasource_type='datasource',
                    datasource_name=parse_return.datasource))
    # process command utils
    elif parse_return.command == 'utils':
        if parse_return.get_memory_info == True:
            print_pretty(obJboss.utils.get_memory_info())
