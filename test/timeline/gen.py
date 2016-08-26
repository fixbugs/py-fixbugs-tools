import random
import string
import sys
if sys.version_info[0] == 3:
    print ("Welcome to qlcoder!")
    print ("We find your Python version is python3.X")
    print ("But this script needs to be executed with Python2.X\n")
    exit()

random.seed(10)
limit = 10000000
out = open('timeline.txt', 'w')
for i in range(limit):
    r = random.randint(1, limit)
    if i % 3 == 0:
        out.write('p ' + str(r) + ' ' + ''.join(random.sample(string.ascii_letters, 4)) + '\r\n')
    else:
        out.write('v ' + str(r) + '\r\n')


#########
# p 2 hello     //素数2发表了1条内容为hello的微博
# p 2 iloveyou
# p 2 heyjuice
# v 10          //数字10查看了自己的时间线，由于10关注了2，因此他看到了这3条微博 heyjuice-iloveyou-hello,按时间的倒序陈列
# p 2 yoyoyo
# p 5 checknow
# v 10          //数字10再次查看了自己的时间线，看到了 checknow-yoyoyo
# v 6           //数字6查看了自己的时间线，由于6关注了2，看到了 yoyoyo-heyjuice-iloveyou-hello
########
