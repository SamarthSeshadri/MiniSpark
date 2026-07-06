from src.models.block import Block
class BlockManager:
    def __init__(self,block_size):
        self.block_size = block_size

    def split_file(self, file_path):
        with open(file_path, 'rb') as file:
            blocks = []
            block_number = 1
            while True:
                chunk = file.read(self.block_size)
                if not chunk:
                    break
                block_id = f"block_{block_number:04d}"
                block = Block(block_id=block_id,data=chunk)
                blocks.append(block)
                block_number += 1
            return blocks

