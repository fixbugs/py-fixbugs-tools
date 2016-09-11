#coding:utf-8
import struct

codeDict = {}#全局字典key=字符，value=数字
encodeDict = {}
filename = None
listForEveryByte = []


class Node:
    def __init__(self, right=None, left=None, parent=None, weight=0, charcode=None):
        self.right = right
        self.left = left
        self.parent = parent
        self.weight = weight
        self.charcode = charcode


#按权值排序

def sort(list):
    return sorted(list, key=lambda node: node.weight)


#构建哈夫曼树
def Huffman(listOfNode):
    listOfNode = sort(listOfNode)
    while len(listOfNode) != 1:
        a, b = listOfNode[0], listOfNode[1]
        new = Node()
        new.weight, new.left, new.right = a.weight + b.weight, a, b
        a.parent, b.parent = new, new
        listOfNode.remove(a), listOfNode.remove(b)
        listOfNode.append(new)
        listOfNode = sort(listOfNode)
    return listOfNode


def inPutFile():
    global filename
    global listForEveryByte
    global codeDict
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
    for k in codeDict:
        listForEveryByte.append(k)
    # filename=raw_input("请输入要压缩的文件：")
    # global  codeDict
    # with open(filename,'rb') as f:
    #     data=f.read()
    #     for Byte in data:
    #         codeDict.setdefault(Byte,0) #每个字节出现的次数默认为0
    #         codeDict[Byte]+=1
    #         listForEveryByte.append(Byte)


def outputCompressedFile():
    global listForEveryByte
    fileString = ""
    with open(filename.split(".")[0]+".jbj", "wb") as f:
        for Byte in listForEveryByte:
            fileString += encodeDict[Byte]  #构成一个长字符序列
        leng = len(fileString)
        more = 16 - leng % 16
        fileString = fileString + "0" * more          #空位用0补齐
        #print(fileString)

        leng = len(fileString)
        i, j = 0, 16
        while j <= leng:
            k = fileString[i:j]
            a = int(k, 2)
            #print(a)
           # print(repr(struct.pack(">H",a)))
            f.write(struct.pack(">H", a))
           # f.write(str(a))
            i = i+16
            j = j+16


def decode(fileString):
    leng = len(fileString)
    more = 16 - leng % 16
    fileString = fileString + "0" * more
    res = list()
    leng = len(fileString)
    i, j = 0, 16
    while j <= leng:
        k = fileString[i:j]
        a = int(k, 2)
        #print(a)
        # print(repr(struct.pack(">H",a)))
        #f.write(struct.pack(">H", a))
        res.append(struct.pack(">H", a))
        # f.write(str(a))
        i = i+16
        j = j+16
    return res


def encode(head, listOfNode):
    global encodeDict
    for e in listOfNode:
        ep = e
        encodeDict.setdefault(e.charcode, "")
        while ep != head:
            if ep.parent.left == ep:
                encodeDict[e.charcode] = "1"+encodeDict[e.charcode]
            else:
                encodeDict[e.charcode] = "0"+encodeDict[e.charcode]
            ep = ep.parent


if __name__ == '__main__':
    inPutFile()
    listOfNode = []
    for e in codeDict.keys():
        listOfNode.append(Node(weight=codeDict[e], charcode=e))
    head = Huffman(listOfNode)[0]
    encode(head, listOfNode)
    print encodeDict
    sstr = '1001111111100111111010011110110011111000101001110110010111110000110010001110101111011100001011111111001000101010010001010111100110100110011100111000011011000111010011010110011111011110101100011110101100100111111000010110111000010001000010101111011100001011101101010010001111100110101110011101000011001110011100010010110110001110101111001001110001011011100001000100001110100011111010110100101011110000110101111111110110111111110010111111001001001000101011110000100100010101001001011111111001111110100011101011110111000001010111100010011010110111010010010110001101101011001001110001011011100001000100000110111011000110000010101111000100110110001111001101101000100010101001000011010111101000101011110000110001001111011000100111011001001110001011011100001000100000100011110011110011010010001010100100010010011111010010001110001100111001110001111100011110010111101100100111001000110011001110101111010001010110111110110001001000011110100011101011110100100101000110001111101010101101010101011100100111001000110011001110101111010001101100011101001101011110111000001111010100011101011110100011011000010001000101110010011100100011001100111010111101001111110011111000110100111010111000111000111110111111100111000101001010010000110010000111101001011110001110101111010010011011110010010010111111100111010111101000100011101100101111100011101011100011100011111011110000111101001100010100111010111101001001010000110110101111111001110101111010010111111011000101000111010111000111000011011000111110101101010100111010111101000101010011011101111110001101110000101111111100111010111101000101101101111101010010010001110101110001110000110011111001100011000100100101001110101111010011000110110000100110011001111011111100011001111011010110010011100111110000100110110010011001101001100111001110000100011111111101101001000101010010001011111101010111101100000111011110001110101111010010100111011001011111000011011000111010011010111111111001111110111101100000111010110111010100101001110110010111110001000101010010001000010001000011101011110100101001110110010111110010100111011110001001101111011001111011100100011101011110100100010100101011011101110000001110101000110101111010111011011100001110101100110111101100110111101001100110010'
4    dres = decode(sstr)
    print ''.join(dres)
#    for d in dres:
#        print d
    # for i in encodeDict.keys():
    #      print (i, encodeDict[i])
