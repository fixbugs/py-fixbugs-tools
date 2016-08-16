#!/usr/bin/env python2.6
#-*- coding: utf-8 -*-

import Queue

from WorkThread import WorkThread


class ThreadQueue(object):
    '''
    query class for exec function
    this is a queue to exec thread things
    1 get all tasks
    2 create work queue and full queue
    3 exec threading and check threading status
    4 put new test into queue where tasks is not null
    5 check tasks is null and all threading is not alive end else go step 3

    work_function 获取任务队列的函数
    function_para 获取任务队列函数的参数
    work_nums 队列长度即同时执行任务的个数
    thread_work_function 任务线程队列的执行函数
    thread_error_file_path 线程队列执行错误的log文件位置


    说明：1、传入的work_function是准备传递给WorkThread的
    2、实例化ThreadQueue类后需要执行添加任务函数add_task
    '''
    def __init__(self, *listl, **kwargs):
        self._is_init = False
        self._flag = True
        if not kwargs:
            self._flag = False
        else:
            if 'work_function' in kwargs and 'thread_work_function' in kwargs:
                self._do_work_function = kwargs['work_function']
                self._thread_work_function = kwargs['thread_work_function']
            else:
                self._flag = False
                pass
            if 'thread_error_file_path' in kwargs:
                self._thread_error_file_path = kwargs['thread_error_file_path']
            else:
                self._thread_error_file_path = '/tmp'\
                                               + '/work_thread_exec_error.log'
            if 'function_para' in kwargs:
                self._function_para = kwargs['function_para']
            if 'work_nums' in kwargs:
                self._work_nums = int(kwargs['work_nums'])
            else:
                self._work_nums = 20
            pass
        pass

    '''
    @return True or False    False need exec again or put para error
    must para
     work_function : you can put in a function or a function with para
                     it maybe empty if use work_function by class init
     function_para : part of work_function
    '''
    def add_tasks(self, **kwargs):
        if not self._flag:
            return False
        if 'work_function' in kwargs:
            work_func = kwargs['work_function']
        else:
            work_func = self._do_work_function
        if not work_func:
            print "ThreadQueue add_tasks need work_function"
            return False
        try:
            if 'function_para' in kwargs:
                self.tasks_list = work_func(**kwargs['function_para'])
            else:
                #check if has put function_para by class init
                if hasattr(self, '_function_para'):
                    self.tasks_list = work_func(**self._function_para)
                else:
                    self.tasks_list = work_func()
        except Exception, e:
            print e
        if not self.tasks_list:
            return False
        self._tasks_total_nums = len(self.tasks_list)
        if self._tasks_total_nums < self._work_nums:
            self._work_nums = self._tasks_total_nums
        #初始化队列
        self._init_queue()
        self._is_init = True
        return True

    '''
    初始后需要循环执行调用的函数
    保证只有当返回值为False时结束调用
    '''
    def do_work(self):
        if not self._is_init:
            self.add_tasks()
        if not self._flag:
            thread_alive_num = 0
            for i in range(0, self._work_nums):
                if not self.thread_arrays[i].isAlive():
                    thread_alive_num += 1
                pass
            if thread_alive_num == self._work_nums:
                print "flag is false and all tasks exec end"
                return True
            print "flag is false end bug tasks need tims to exec"
            return False
        #sencond init task queue and create thread arrays
        for i in range(0, self._work_nums):
            if len(self.thread_arrays) < self._work_nums:
                #先判断队列是否为空以及_tasks_list_num即当前标记num的数值
                if self.queue.empty():
                    self._full_queue()
                    pass
                work_thread = WorkThread(
                    work_function=self._thread_work_function,
                    error_file_path=self._thread_error_file_path,
                    function_para=self.queue.get())
                work_thread.start()
                self.thread_arrays.append(work_thread)
                #取出了队列中的元素后补足队列
                self._full_queue()
            else:
                if not self.thread_arrays[i].isAlive():
                    if self.queue.empty():
                        #只有当队列再次为空时 全局程序才结束
                        self._flag = False
                        break
                    else:
                        work_thread = WorkThread(
                            work_function=self._thread_work_function,
                            error_file_path=self._thread_error_file_path,
                            function_para=self.queue.get())
                        work_thread.start()
                        #更新替换已经死亡的thread
                        self.thread_arrays[i] = work_thread
                    if self.queue.qsize() < self._work_nums:
                        if self._tasks_list_num == self._tasks_total_nums:
                            #只有当前任务num和队列初始总数想当时才断开判断，不再填充队列
                            break
                        self._full_queue()
        return True

    '''
    stop queue task add into thread
    '''
    def stop(self):
        self._flag = False

    '''
    @return none
    explain: if just can use by self function and juse once
    '''
    def _init_queue(self):
        self.queue = Queue.Queue(maxsize=self._work_nums)
        self.thread_arrays = []
        self._tasks_list_num = 0
        if hasattr(self, 'tasks_list') and len(self.tasks_list):
            self._full_queue()

    '''
    添加任务到队列里
    @return boolen True means self queue has full else False means other
    '''
    def _full_queue(self):
        if self._tasks_list_num == self._tasks_total_nums:
            return False
        if self.queue.empty() or self.queue.qsize() < self._work_nums:
            for i in range(self.queue.qsize(), self._work_nums):
                #向queue里增加任务，初始时queue为空
                self.queue.put(self.tasks_list[self._tasks_list_num])
                self._tasks_list_num += 1
        return True

    #获取当前队列,只返回队列句柄
    def getWorkingQueue(self):
        return self.queue
