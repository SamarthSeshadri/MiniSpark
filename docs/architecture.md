# MiniSpark Architecture

## Sprint 1 - Block

### Problem

Large files cannot be efficiently stored or processed on a single machine.

### Solution

Split files into smaller fixed-size blocks.

### Responsibilities of a Block

- Represent one chunk of a file.
- Store the block's data.
- Store basic metadata.

### Non-Responsibilities

A Block should NOT:
- Know which DataNode stores it.
- Know about replication.
- Communicate with the NameNode.