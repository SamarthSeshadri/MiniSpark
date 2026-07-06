from src.services.block_manager import BlockManager


def test_split_file():

    manager = BlockManager(block_size=4)

    blocks = manager.split_file("datasets/sample.txt")

    assert len(blocks) == 3

    assert blocks[0].block_id == "block_0001"
    assert blocks[0].data == b"ABCD"
    assert blocks[0].size == 4

    assert blocks[1].block_id == "block_0002"
    assert blocks[1].data == b"EFGH"
    assert blocks[1].size == 4

    assert blocks[2].block_id == "block_0003"
    assert blocks[2].data == b"IJ"
    assert blocks[2].size == 2