from dataclasses import dataclass

@dataclass
class Block:
    block_id: str
    data: bytes

    @property
    def size(self):
        return len(self.data)