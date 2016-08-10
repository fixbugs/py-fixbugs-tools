#!/usr/bin/env python


def get_data(num=2333):
    count = 0
    for i in range(2, 10000):
        if i % 2 == 0 or i % 3 == 0:
            count += 1
        if count == num:
            return i
    return False

#print get_data()


def box(data, max_num):
    box_arr = []
    tag_arr = []
    d_len = len(data)
    for i in range(0, max_num):
        tmp = dict()
        tmp['weight'] = 0
        tmp['mark'] = list()
        for j in range(0, d_len):
            tmp['mark'].append(False)
        tag_arr.append(tmp)
    for i in range(0, d_len):
        j = max_num - 1
        while True:
            if not j:
                break
            if j < data[i]:
                break
            if tag_arr[j]['weight'] < tag_arr[j - data[i]]['weight'] + data[i]:
                tag_arr[j]['weight'] = tag_arr[j - data[i]]['weight'] + data[i]
                for k in range(0, d_len):
                    tag_arr[j]['mark'][k] = tag_arr[j - data[i]]['mark'][k]
                tag_arr[j]['mark'][i] = True
            j = j - 1
    flag = 1
    for i in range(0, d_len):
        if(flag and tag_arr[max_num - 1]['mark'][i]):
            box_arr.append(i + 1)
            flag = 0
            continue
        if(tag_arr[max_num - 1]['mark'][i]):
            box_arr.append(i + 1)
    result = dict()
    result['weight'] = tag_arr[max_num - 1]['weight']
    result['box_link'] = '-'.join(map(str, box_arr))
    return result

# hd_arr = [509, 838, 924, 650, 604, 793, 564, 651, 697, 649, 747, 787, 701, 605, 644]
# max_num = 5000
# print box(hd_arr, max_num)


def get_pass(pass_md5):
    pass_md5 = pass_md5.lower()
    import hashlib
    pass_str = ''
    for i in range(1990,2016):
        for j in range(1,12):
            for k in range(1,31):
                y = str(i)
                m = '0'+str(j) if j<10 else str(j)
                d = '0'+str(k) if k<10 else str(k)
                tmp_str = y+m+d
                if hashlib.md5(tmp_str).hexdigest() == pass_md5:
                    return tmp_str

print get_pass('7E38890B870934B126F66857ED6B57B9')
