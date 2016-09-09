mp = {}
# user_code
def get(key):
    key = createNewKey(key)
    return heightToInt(mp.get(key, 0))

def put(key):
    last_key = key
    key = createNewKey(key)
    last_num = get(last_key)
    mp[key] = intToHeight(last_num + 1)
    s = ''
    for kv in mp.items():
        s = '%s:%s\n' % kv + s
    b_s = bytearray(s)
    write_file(0, b_s)


def init():
    ls = map(chr, read_file(0, 102400))
    for li in ''.join(ls).split('\n'):
        l2 = li.split(':')
        if len(l2)<2:
            continue
        mp[l2[0]] = str(l2[1])

def createNewKey(key):
    if len(key) < 8 :
        return key
    import hashlib
    hash_key = hashlib.md5(key).hexdigest()
    hash_key = hashlib.md5(has_key + key).hexdigest()
    result = hash_key[0:8]
    return result

def intToHeight(num):
    loop = '0123456789abcdefghijklmnopqrstuvwxyz'
    a = []
    while num != 0:
        a.append(loop[num % 36])
        num = num / 36
    a.reverse()
    return ''.join(a)


def heightToInt(nstr):
    nstr = str(nstr)
    loop = '0123456789abcdefghijklmnopqrstuvwxyz'
    res = 0
    length = len(nstr)
    for i in range(length)[::-1]:
        res += loop.index(nstr[i]) * pow(36, length-i-1)
    return res
