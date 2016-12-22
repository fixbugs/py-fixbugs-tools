#!/usr/bin/env python
#coding=utf8

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

try:
  #建立socket
    transport = TSocket.TSocket('121.201.63.168', 9090)
    #选择传输层，这块要和服务端的设置一致
    transport = TTransport.TBufferedTransport(transport)
    #选择传输协议，这个也要和服务端保持一致，否则无法通信
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    #创建客户端
    client = HelloWorld.Client(protocol)
    client = Task.getTaskInfo()
    transport.open()

    print "client - ping"
    print "server - " + client.ping()

    print "client - say"
    msg = client.say("Hello!")
    print "server - " + msg
    #关闭传输
    transport.close()
#捕获异常
except Thrift.TException, ex:
    print "%s" % (ex.message)
