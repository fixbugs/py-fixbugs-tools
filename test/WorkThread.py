#!/usr/bin/env python2.6
#-*- coding: utf-8 -*-

import threading
import simplejson


class WorkThread(threading.Thread):
    '''
    work thread class
    input: kwargs(dict)
    output: None but exec function input in

    explain:
        do_method : exec work_function times, now just can be once
    '''
    def __init__(self, **kwargs):
        threading.Thread.__init__(self)
        self._m_stop = False
        if not kwargs:
            self._m_stop = True
        else:
        #work_function,errof_file_path,do_method='once'
            if 'error_file_path' in kwargs and 'work_function' in kwargs:
                self._error_file_path = kwargs['error_file_path']
                self._do_work_function = kwargs['work_function']
            else:
                self._m_stop = True
            if 'do_method' in kwargs:
                self._do_method = kwargs['do_method']
            else:
                self._do_method = 'once'
            if 'function_para' in kwargs:
                self._function_para = kwargs['function_para']

    '''
    线程方法重写，单独使用线程方法
    '''
    def run(self):
        while not self._m_stop:
            if hasattr(self, '_function_para'):
                if isinstance(self._function_para, dict):
                    res = self._do_work_function(**self._function_para)
                elif isinstance(self._function_para, list):
                    res = self._do_work_function(*self._function_para)
                elif isinstance(self._function_para, tuple):
                    res = self._do_work_function(*self._function_para)
                elif isinstance(self._function_para, str):
                    res = self._do_work_function(self._function_para)
                else:
                    self.stop()
                    res = True
            else:
                res = self._do_work_function()
            #check if need add errorlog
            if not res:
                if hasattr(self, '_function_para'):
                    line_data = 'error function return'\
                                + ' False with params:'\
                                + '%s\n' % (
                                    simplejson.dumps(self._function_para))
                else:
                    line_data = 'error function return False \n'
                self._errorLogWrite(line_data)
            elif isinstance(res, dict):
                if not res['status']:
                    line_data = 'message' in res if True else 'error'
                    + 'with get message'
                    if hasattr(self, '_function_para'):
                        line_data = 'error by' + str(line_data)
                        + 'with params:%s \n'
                        + '' % (simplejson.dumps(self._function_para))
                    else:
                        line_data = str(line_data) + '\n'
                    self._errorLogWrite(line_data)
            if self._do_method == 'once':
                self.stop()

    '''
    wirth something into error_file_path if need
    '''
    def _errorLogWrite(self, line_data):
        if not self._error_file_path:
            return
        file_handle = None
        try:
            file_handle = open(self._error_file_path, 'a')
            file_handle.write(str(line_data))
        finally:
            if not file_handle:
                return
            file_handle.close()

    '''
    stop thread run if need
    '''
    def stop(self):
        self._m_stop = True
