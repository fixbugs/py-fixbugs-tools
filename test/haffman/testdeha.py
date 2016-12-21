#-*- coding:utf-8 -*-
import six
import sys

class HuffNode(object):
    """
    定义一个HuffNode虚类，里面包含两个虚方法：
    1. 获取节点的权重函数
    2. 获取此节点是否是叶节点的函数

    """
    def get_wieght(self):
        raise NotImplementedError(
            "The Abstract Node Class doesn't define 'get_wieght'")

    def isleaf(self):
        raise NotImplementedError(
            "The Abstract Node Class doesn't define 'isleaf'")


class LeafNode(HuffNode):
    """
    树叶节点类
    """
    def __init__(self, value=0, freq=0,):
        """
        初始化 树节点 需要初始化的对象参数有 ：value及其出现的频率freq
        """
        super(LeafNode, self).__init__()
        # 节点的值
        self.value = value
        self.wieght = freq


    def isleaf(self):
        """
        基类的方法，返回True，代表是叶节点
        """
        return True

    def get_wieght(self):
        """
        基类的方法，返回对象属性 weight，表示对象的权重
        """
        return self.wieght

    def get_value(self):
        """
        获取叶子节点的 字符 的值
        """
        return self.value


class IntlNode(HuffNode):
    """
    中间节点类
    """
    def __init__(self, left_child=None, right_child=None):
        """
        初始化 中间节点 需要初始化的对象参数有 ：left_child, right_chiled, weight
        """
        super(IntlNode, self).__init__()

        # 节点的值
        self.wieght = left_child.get_wieght() + right_child.get_wieght()
        # 节点的左右子节点
        self.left_child = left_child
        self.right_child = right_child


    def isleaf(self):
        """
        基类的方法，返回False，代表是中间节点
        """
        return False

    def get_wieght(self):
        """
        基类的方法，返回对象属性 weight，表示对象的权重
        """
        return self.wieght

    def get_left(self):
        """
        获取左孩子
        """
        return self.left_child

    def get_right(self):
        """
        获取右孩子
        """
        return self.right_child


class HuffTree(object):
    """
    huffTree
    """
    def __init__(self, flag, value =0, freq=0, left_tree=None, right_tree=None):

        super(HuffTree, self).__init__()

        if flag == 0:
            self.root = LeafNode(value, freq)
        else:
            self.root = IntlNode(left_tree.get_root(), right_tree.get_root())


    def get_root(self):
        """
        获取huffman tree 的根节点
        """
        return self.root

    def get_wieght(self):
        """
        获取这个huffman树的根节点的权重
        """
        return self.root.get_wieght()

    def traverse_huffman_tree(self, root, code, char_freq):
        """
        利用递归的方法遍历huffman_tree，并且以此方式得到每个 字符 对应的huffman编码
        保存在字典 char_freq中
        """
        if root.isleaf():
            char_freq[root.get_value()] = code
            print ("it = %c  and  freq = %d  code = %s")%(chr(root.get_value()),root.get_wieght(), code)
            return None
        else:
            self.traverse_huffman_tree(root.get_left(), code+'0', char_freq)
            self.traverse_huffman_tree(root.get_right(), code+'1', char_freq)



def buildHuffmanTree(list_hufftrees):
    """
    构造huffman树
    """
    while len(list_hufftrees) >1 :

        # 1. 按照weight 对huffman树进行从小到大的排序
        list_hufftrees.sort(key=lambda x: x.get_wieght()) 

        # 2. 跳出weight 最小的两个huffman编码树
        temp1 = list_hufftrees[0]
        temp2 = list_hufftrees[1]
        list_hufftrees = list_hufftrees[2:]

        # 3. 构造一个新的huffman树
        newed_hufftree = HuffTree(1, 0, 0, temp1, temp2)

        # 4. 放入到数组当中
        list_hufftrees.append(newed_hufftree)

    # last.  数组中最后剩下来的那棵树，就是构造的Huffman编码树
    return list_hufftrees[0]

def decompress(inputfilename, outputfilename):
    """
    解压缩文件，参数有 
    inputfilename：压缩文件的地址和名字
    outputfilename：解压缩文件的存放地址和名字
    """
    # 读取文件
    # f = open(inputfilename,'rb')
    # filedata = f.read()
    # # 获取文件的字节总数
    # filesize = f.tell()

    # # 1. 读取压缩文件中保存的树的叶节点的个数
    # # 一下读取 4个 字节，代表一个int型的值
    # a1 = six.byte2int(filedata[0])
    # a2 = six.byte2int(filedata[1])
    # a3 = six.byte2int(filedata[2])
    # a4 = six.byte2int(filedata[3])
    # j = 0
    # j = j|a1
    # j = j<<8
    # j = j|a2
    # j = j<<8
    # j = j|a3
    # j = j<<8
    # j = j|a4

    # leaf_node_size = j


    # # 2. 读取压缩文件中保存的相信的原文件中 ［0-255］出现的频率的信息
    # # 构造一个 字典 char_freq 一遍重建 Huffman编码树
    # char_freq = {}
    # for i in range(leaf_node_size):
    #     c = six.byte2int(filedata[4+i*5+0])

    #     # 同样的，出现的频率是int型的，读区四个字节来读取到正确的数值
    #     a1 = six.byte2int(filedata[4+i*5+1])
    #     a2 = six.byte2int(filedata[4+i*5+2])
    #     a3 = six.byte2int(filedata[4+i*5+3])
    #     a4 = six.byte2int(filedata[4+i*5+4])
    #     j = 0
    #     j = j|a1
    #     j = j<<8
    #     j = j|a2
    #     j = j<<8
    #     j = j|a3
    #     j = j<<8
    #     j = j|a4
    #     print c, j
    #     char_freq[c] = j
    codeDict = dict()

    codeDict[' '] = 100
    codeDict[','] = 7
    codeDict['.'] = 10
    codeDict['a'] = 36
    codeDict['b'] = 3
    codeDict['c'] = 8
    codeDict['d'] = 18
    codeDict['e'] = 42
    codeDict['f'] = 6
    codeDict['g'] = 13
    codeDict['h'] = 40
    codeDict['i'] = 31
    codeDict['j'] = 1
    codeDict['k'] = 3
    codeDict['l'] = 25
    codeDict['m'] = 11
    codeDict['n'] = 36
    codeDict['o'] = 23
    codeDict['p'] = 3
    codeDict['q'] = 1
    codeDict['r'] = 20
    codeDict['s'] = 25
    codeDict['t'] = 45
    codeDict['u'] = 3
    codeDict['v'] = 1
    codeDict['w'] = 14
    codeDict['x'] = 1
    codeDict['y'] = 5
    codeDict['z'] = 1

    char_freq = codeDict
    # 3. 重建huffman 编码树，和压缩文件中建立Huffman编码树的方法一致
    list_hufftrees = []
    for x in char_freq.keys():
        tem = HuffTree(0, x, char_freq[x], None, None)
        list_hufftrees.append(tem)

    tem = buildHuffmanTree(list_hufftrees)
    tem.traverse_huffman_tree(tem.get_root(),'',char_freq)




    # 4. 使用步骤3中重建的huffman编码树，对压缩文件进行解压缩
    output = open(outputfilename, 'wb')
    code = ''
    currnode = tem.get_root()
    for x in range(leaf_node_size*5+4,filesize):

        c = six.byte2int(filedata[x])
        for i in range(8):
            if c&128:
                code = code +'1'
            else:
                code = code + '0'
            c = c<<1

        while len(code) > 24:
            if currnode.isleaf():
                tem_byte = six.int2byte(currnode.get_value())
                output.write(tem_byte)
                currnode = tem.get_root()

            if code[0] == '1':
                currnode = currnode.get_right()
            else:
                currnode = currnode.get_left()
            code = code[1:]


    # 4.1 处理最后 24位
    sub_code = code[-16:-8]
    last_length = 0
    for i in range(8):
        last_length = last_length<<1
        if sub_code[i] == '1':
            last_length = last_length|1

    code = code[:-16] + code[-8:-8 + last_length]

    while len(code) > 0:
            if currnode.isleaf():
                tem_byte = six.int2byte(currnode.get_value())
                output.write(tem_byte)
                currnode = tem.get_root()

            if code[0] == '1':
                currnode = currnode.get_right()
            else:
                currnode = currnode.get_left()
            code = code[1:]

    if currnode.isleaf():
        tem_byte = six.int2byte(currnode.get_value())
        print tem_byte
        output.write(tem_byte)
        currnode = tem.get_root()

    # 4. 关闭文件，解压缩完毕
    output.close()
