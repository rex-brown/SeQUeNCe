from typing import Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from ...topology.node import Node

from ..message import Message
from ..protocol import StackProtocol


class StaticRoutingMessage(Message):
    def __init__(self, msg_type: str, receiver: str, payload: "Message"):
        super().__init__(msg_type, receiver)
        self.payload = payload


class StaticRoutingProtocol(StackProtocol):
    def __init__(self, own: "Node", name: str, forwarding_table: Dict):
        '''
        forwarding_table: {name of destination node: name of next node}
        '''
        super().__init__(own, name)
        self.forwarding_table = forwarding_table

    def add_forwarding_rule(self, dst: str, next_node: str):
        assert dst not in self.forwarding_table
        self.forwarding_table[dst] = next_node

    def push(self, **kwargs):
        dst = kwargs["dst"]
        kwargs["dst"] = self.forwarding_table[dst]
        self._push(**kwargs)

    def pop(self, **kwargs):
        self._pop(**kwargs)

    def received_message(self, src: str, msg: "Message"):
        raise Exception("RSVP protocol should not call this function")

    def init(self):
        pass
