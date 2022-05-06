import struct

STATUS_DELETED = 0
STATUS_REGULAR = 2

# todo: not implemented -> see https://gordthompson.github.io/ov2optimizer/ov2FileFormat.html for more detail
# STATUS_SKIPPER = 1
# STATUS_EXTENDED = 3


def serialize(lon, lat, label, status=STATUS_REGULAR):
    size = 14 + len(label)
    lon = int(lon * 100000)
    lat = int(lat * 100000)
    label = label.encode('utf8')
    buff = struct.pack(f'<B3i{len(label) + 1}s', status, size, lon, lat, label)
    return buff


def deserialize(buff):
    status, size, lon, lat, label = struct.unpack(f'<B3i{len(buff) - 14}sx', buff)
    lon /= 100000
    lat /= 100000
    label = label.decode()
    return lon, lat, label, status
