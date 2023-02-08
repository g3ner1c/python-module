import importlib.metadata

from qbreader.api import (
    num_packets,
    packet,
    packet_bonuses,
    packet_tossups,
    query,
    random_name,
    random_question,
    report_question,
    room_list,
    set_list,
)

__version__ = importlib.metadata.version("qbreader")

del importlib
