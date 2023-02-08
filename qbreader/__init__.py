import importlib.metadata

from .quizbowlAPI import query, random_question, random_name, packet, packet_bonuses, packet_tossups, num_packets, set_list, room_list, report_question

__version__ = importlib.metadata.version("qbreader")

del importlib
