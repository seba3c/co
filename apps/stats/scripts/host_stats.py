# -*- coding: utf-8 -*-


def host_stats_dict():
    import sys
    import psutil
    import socket
    
    stats = {}
    stats['cpu_percent'] = psutil.cpu_percent()
    stats['total_uptime'] = psutil.boot_time()

    mem = psutil.virtual_memory()
    stats['mem_total'] = mem.total
    stats['mem_available'] = mem.available
    stats['mem_percent'] = mem.percent
    stats['mem_used'] = mem.used
    stats['mem_free'] = mem.free
    stats['mem_active'] = mem.active
    stats['mem_inactive'] = mem.inactive
    stats['mem_buffers'] = mem.buffers
    stats['mem_cached'] = mem.cached
    stats['mem_shared'] = mem.shared

    stats["os_name"] = sys.platform
    stats["host_name"] = socket.gethostname()

    return stats


def host_stats():
    return str(host_stats_dict())


if __name__ == '__main__':
    stats = host_stats_dict()
    for k, v in stats.items():
        print("%s:%s" % (k,v))
