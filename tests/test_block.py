from src.models.block import Block

def test_block():
    block = Block("block1",b"hello")

    assert block.block_id == "block1"
    assert block.data == b"hello"
    assert block.size == 5
