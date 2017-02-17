#!/usr/bin/env python
# -*- coding: utf-8 -*-

# E-mail: windcao@hotmail.com
# https://github.com/caojianfeng/vnet
__author__ = 'caojianfeng'

import time
import os
import sched


# 初始化sched模块的scheduler类
# 第一个参数是一个可以返回时间戳的函数，第二个参数可以在定时未到达之前阻塞。
schedule = sched.scheduler(time.time, time.sleep)


# 被周期性调度触发的函数
def execute_command(cmd, inc):
    '''''
    终端上显示当前计算机的连接情况
    '''
    os.system(cmd)
    schedule.enter(inc, 0, execute_command, (cmd, inc))


def main(cmds, inc=60):
    # enter四个参数分别为：间隔事件、优先级（用于同时间到达的两个事件同时执行时定序）、被调用触发的函数，
    # 给该触发函数的参数（tuple形式）
    for cmd in cmds:
        schedule.enter(0, 0, execute_command, (cmd, inc))

    schedule.run()


# 每60秒查看下网络连接情况
if __name__ == '__main__':
    curl_header =  "curl -o /dev/null -w %{time_connect}::%{time_starttransfer}::%{time_total}\"\n\" --connect-timeout 4 -m 4 ";
    cmds = [
        curl_header+" \"http://10.169.105.46:8880/v3/app/android/phone/animation?argCon=0&page=XXX\""
        ,curl_header+" \"http://gundam.ovo.top/api/test.php?uid=S1427347837&cert=c79b18d383c8675bfce0b7fb1d520949\""
    ]

    main(cmds, 60)


