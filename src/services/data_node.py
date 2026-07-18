from pathlib import Path
from src.models.block import Block
class DataNode:
    def __init__(self, storage_path):
        self.storage_path = Path(storage_path)
        self.storage_path.mkdir(parents=True,exist_ok=True)

    def store_block(self,block):
        block_path = self.storage_path / f"{block.block_id}.bin"
        with open(block_path,'wb') as file:
            file.write(block.data)
    def get_block(self,block_id):
        block_path = self.storage_path / f"{block_id}.bin"
        with open(block_path,'rb') as file:
            data = file.read()
        return Block(block_id=block_id,data=data)
    def delete_block(self,block_id):
        block_path = self.storage_path / f"{block_id}.bin"
        try:
            block_path.unlink()   
        except FileNotFoundError:
            pass        
    def has_block(self,block_id):
        block_path = self.storage_path / f"{block_id}.bin"
        return block_path.exists()
    def list_blocks(self):
        blocks = []
        for block_file in self.storage_path.glob("*.bin*"):
            blocks.append(block_file.stem)

        return blocks


