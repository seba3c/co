# -*- coding: utf-8 -*-


def host_stats_dict():

    import psutil
    stats = {'cpu': {}, 'mem': {}}
    stats['cpu']['percent'] = psutil.cpu_percent()

    mem = psutil.virtual_memory()
    stats['mem']['total'] = mem.total
    stats['mem']['available'] = mem.available
    stats['mem']['percent'] = mem.percent
    stats['mem']['used'] = mem.used
    stats['mem']['free'] = mem.free
    stats['mem']['active'] = mem.active
    stats['mem']['inactive'] = mem.inactive
    stats['mem']['buffers'] = mem.buffers
    stats['mem']['cached'] = mem.cached
    stats['mem']['shared'] = mem.shared

    return stats


def host_stats():
    return str(host_stats_dict())


if __name__ == '__main__':
    print(host_stats())
