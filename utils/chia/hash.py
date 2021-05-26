import blspy

from utils.chia.sized_bytes import bytes32


def std_hash(b) -> bytes32:
    """
    The standard hash used in many places.
    """
    return bytes32(blspy.Util.hash256(bytes(b)))
