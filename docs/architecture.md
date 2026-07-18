# MiniSpark Architecture

MiniSpark is a simplified implementation of a distributed data processing ecosystem inspired by Hadoop HDFS and Apache Spark.

The purpose of this project is not to recreate Hadoop feature-for-feature, but to understand the engineering decisions behind distributed storage, metadata management, task scheduling, and distributed computation by implementing each component from scratch.

---

# Sprint 1 - Block

## Problem

Large files cannot be efficiently stored or processed as a single unit in distributed systems.

A distributed filesystem requires files to be divided into smaller independent pieces that can be stored across multiple machines.

---

## Solution

Introduce a Block object that represents a fixed-size chunk of a file.

Each block contains only its own data and identifier.

---

## Responsibilities

A Block is responsible for:

- Representing a single chunk of a file
- Storing raw binary data
- Maintaining its unique block identifier

---

## Non-Responsibilities

A Block should NOT:

- Know which DataNode stores it
- Know about replication
- Know about other blocks
- Communicate with the NameNode
- Perform file splitting

---

## Engineering Decisions

### Why bytes instead of strings?

Distributed storage systems store arbitrary files:

- Images
- Videos
- PDFs
- Databases
- CSVs

Therefore blocks store raw bytes instead of text.

---

### Why use a dataclass?

A Block is primarily a data container.

Using Python's dataclass removes boilerplate while keeping the model simple.

---

### Why is size a property?

The size is always derived from the stored data.

Maintaining a separate size field could introduce inconsistencies.

The block should always compute its size dynamically.

---

# Sprint 2 - BlockManager

## Problem

Applications should not manually divide files into blocks.

The logic for splitting files should be centralized.

---

## Solution

Introduce a BlockManager responsible for converting files into Block objects.

---

## Responsibilities

BlockManager is responsible for:

- Reading files
- Splitting files into fixed-size chunks
- Creating Block objects
- Generating block identifiers

---

## Non-Responsibilities

BlockManager should NOT:

- Store blocks
- Decide block placement
- Communicate with DataNodes
- Manage replication
- Maintain metadata

---

## Engineering Decisions

### Why read files in binary mode?

Reading in binary mode allows MiniSpark to support every file type instead of only text files.

---

### Why read files in chunks?

Loading an entire file into memory is inefficient for large files.

Chunked reading keeps memory usage predictable and scalable.

---

### Why generate block IDs?

Each block requires a unique identifier so that metadata systems can reference it independently of the original file.

---

# Sprint 3 – DataNode

## Problem

Blocks currently exist only in memory.

Distributed storage requires blocks to persist on disk.

---

## Solution

Introduce the DataNode.

The DataNode stores, retrieves, deletes, and manages block files on disk.

---

## Responsibilities

A DataNode is responsible for:

- Persisting blocks
- Retrieving stored blocks
- Deleting blocks
- Reporting which blocks it stores

---

## Non-Responsibilities

A DataNode should NOT:

- Know about complete files
- Split files
- Decide where blocks should be stored
- Manage replication
- Maintain global metadata

---

## Engineering Decisions

### Why store blocks as .bin files?

The `.bin` extension is used purely for readability.

The block contents are raw bytes regardless of the filename extension.

---

### Why reconstruct Block objects?

The DataNode API stores and returns Block objects.

The internal storage format remains hidden from callers.

---

### Why use pathlib?

`pathlib` provides an object-oriented interface for filesystem operations and produces cleaner, more portable code than string-based path manipulation.

---

### Why expose has_block()?

Checking for block existence should not require opening the block file.

Providing a dedicated existence check keeps the API efficient and expressive.

---

## Current Architecture

Client

↓

BlockManager

↓

Block Objects

↓

DataNode

↓

Disk