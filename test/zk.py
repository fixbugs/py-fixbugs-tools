#coding=utf8

from kazoo.client import KazooClient

zk = KazooClient(hosts='121.201.8.217:2181')
zk.start()
print zk.get("/qlcoder/zookeeper")
