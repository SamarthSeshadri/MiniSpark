from src.services.data_node import DataNode
from src.models.block import Block

def test_store_block(tmp_path):
    node = DataNode(tmp_path)
    block = Block(block_id="block_0001", data = b"Hello MiniSpark")

    node.store_block(block)
    block_path = tmp_path / "block_0001.bin"
    assert block_path.exists()

def test_get_block(tmp_path):
    # Arrange
    node = DataNode(tmp_path)
    original_block = Block(
        block_id="block_0001",
        data=b"Hello MiniSpark"
    )

    node.store_block(original_block)

    # Act
    retrieved_block = node.get_block("block_0001")

    # Assert
    assert retrieved_block.block_id == original_block.block_id
    assert retrieved_block.data == original_block.data   

def test_has_block(tmp_path):
    node = DataNode(tmp_path)
    block = Block(block_id="block_0001", data=b"Hello MiniSpark")
    node.store_block(block)
    assert node.has_block("block_0001") == True

def test_delete_block(tmp_path):
    # Arrange
    node = DataNode(tmp_path)
    block = Block(
        block_id="block_0001",
        data=b"Hello MiniSpark"
    )

    node.store_block(block)

    # Act
    node.delete_block("block_0001")

    # Assert
    assert not node.has_block("block_0001")

def test_list_blocks(tmp_path):
    # Arrange
    node = DataNode(tmp_path)

    block1 = Block(
        block_id="block_0001",
        data=b"Hello"
    )

    block2 = Block(
        block_id="block_0002",
        data=b"MiniSpark"
    )

    node.store_block(block1)
    node.store_block(block2)

    # Act
    blocks = node.list_blocks()

    # Assert
    assert len(blocks) == 2
    assert "block_0001" in blocks
    assert "block_0002" in blocks
    