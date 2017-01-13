def wheelerTransform(data):
    data = "^" + data + "|"
    length = len(data)
    rotations = []
    for i in range(length, 0, -1):
        rotations.append(data[i:length] + data[0:i])
    rotations.sort()
    result = ""
    for r in rotations:
        result += r[length - 1]
    return result


def compress(data):
    result = ""
    count = 1
    cur = data[0]
    for d in data[1:]:
        if(d != cur):
            result += cur + str(count)
            count = 1
            cur = d
        else:
            count += 1
    return result + cur + str(count)


if __name__=='__main__':
    wt = wheelerTransform("BABABABANANABABABABABANANABABABABABANANABANANANAAHH")
    print wt
    print compress(wt)
