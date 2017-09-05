# coding=utf-8

# 多进程

# Python的os模块封装了常见的系统调用，其中就包括fork：
# 下面这种情况适用于linux,unix以及mac系统
# import os
#
# print 'Process (%s) start...' % os.getpid()
# pid = os.fork()
# if pid == 0:
#     print 'I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid())
# else:
#     print 'I (%s) just created a child process (%s).' % (os.getpid(), pid)
# print

# 由于Python是跨平台的，自然也应该提供一个跨平台的多进程支持。
# multiprocessing模块就是跨平台版本的多进程模块。
# multiprocessing模块提供了一个Process类来代表一个进程对象，下面的例子演示量启动一个子进程并等待其结束：
# from multiprocessing import Process
# import os
#
# # 子进程要执行的代码
# def run_proc(name):
#     print 'Run child process %s (%s)...' % (name, os.getpid())
# if __name__ == '__main__':
#     print 'Parent process %s.' % os.getpid()
#     p = Process(target=run_proc, args=('test',))
#     print 'Process will start.'
#     p.start()  # 启动进程
#     p.join()  # 等待子进程结束后再继续往下运行，通常用于进程间的同步
#     print 'Process end.'

###########################################
# Pool
# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
# 对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
# 对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
# 请注意输出的结果，task 0，1，2，3是立刻执行的，而task 4要等待前面某个task完成后才执行，这是因为Pool的默认大小在我的电脑上是4，因此，最多同时执行4个进程。这是Pool有意设计的限制，并不是操作系统的限制。
# from multiprocessing import Pool
# import os, time, random
#
# def long_time_task(name):
#     print 'Run task %s (%s)...' % (name, os.getpid())
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print 'Task %s runs %0.2f seconds.' % (name, end - start)
#
# if __name__ == '__main__':
#     print 'Parent process %s.' % os.getpid()
#     p = Pool()
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print 'Waiting for all subprocesses done...'
#     p.close()
#     p.join()
#     print 'All subprocesses done.'


#####################################################
# 进程间通信
# Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。
# Python的multiprocessing模块包装了底层的机制，提供了Queue,Pipes等多种方式来交换数据。
# 下面以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据：
# from multiprocessing import Process, Queue
# import os, time, random
#
# # 写数据进程执行的代码：
# def write(q):
#     for value in ['A', 'B', 'C']:
#         print 'Put %s to queue...' % value
#         q.put(value)
#         time.sleep(random.random())
#
# # 读数据进程执行的代码：
# def read(q):
#     while True:
#         value = q.get(True)
#         print 'Get %s from queue.' % value
#
# if __name__ == '__main__':
#     # 父进程创建Queue，并传给各个子进程
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     # 启动子进程pw，写入：
#     pw.start()
#     # 启动子进程pr，读取：
#     pr.start()
#     # 等待pw结束：
#     pw.join()
#     # pr进程里是死循环，无法等待其结束，只能强制终止：
#     pr.terminate()
