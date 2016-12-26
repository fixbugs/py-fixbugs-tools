#!/usr/bin/env python
#coding=utf8

import sys
import glob
sys.path.append('gen-py')
#sys.path.insert(0, glob.glob('../../lib/py/build/lib*')[0])
#sys.path.insert(0, glob.glob('/html/NginxServer/py-fixbugs-tools/test/rpc/gen-py/task7698'))
#sys.path.insert(0, '/html/NginxServer/py-fixbugs-tools/test/rpc/gen-py/task7698')
sys.path.append('/html/NginxServer/py-fixbugs-tools/test/rpc/')
#sys.path.append


from task7698 import Task
from task7698.ttypes import Auth

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
    client = Task.Client(protocol)
    transport.open()
    aub = Auth('fixbug', 1)
    print aub
    msg = client.getTaskInfo(aub)
    print msg
        #关闭传输
    transport.close()
#捕获异常
except Thrift.TException, ex:
    print "%s" % (ex.message)
#545de5394559dcd16e2acd207bc929aa
