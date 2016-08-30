from machinetalk.protobuf.firmware_pb2 import Firmware, Connector
from util import get_git_revision_short_hash, get_build_url


def gen_fwid(*args,**kwargs):
    # construct the descriptor object
    fw  = Firmware()
    fw.build_sha = get_git_revision_short_hash()
    fw.comment = get_build_url()

    fw.fpga_part_number = "7z020"
    fw.num_leds = 3
    fw.board_name = "ZTIO"

    c = fw.connector.add()
    c.name = "U20"
    c.pins = 4

    c = fw.connector.add()
    c.name = "J6"
    c.pins = 8

    c = fw.connector.add()
    c.name = "J5"
    c.pins = 8

    c = fw.connector.add()
    c.name = "J3"
    c.pins = 36

    c = fw.connector.add()
    c.name = "J7"
    c.pins = 8

    return fw

