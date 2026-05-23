# Multi-Chain Wallet Scanner

A professional Python script for blockchain researchers and developers to instantly audit wallet holdings across multiple networks. By leveraging asynchronous programming, this tool fetches data in parallel, significantly reducing execution time compared to sequential scanning.

## Key Features
- **Cross-Chain Support:** Pre-configured for Ethereum, Binance Smart Chain, and Polygon.
- **Async Execution:** Uses `asyncio` and `aiohttp` for high-performance RPC calls.
- **Human Readable:** Automatically converts Wei to Ether/Token units for clarity.
- **Flat Design:** Single-script implementation for easy portability and zero-config usage.

## Setup Instructions
1. Install requirements: `pip install web3 aiohttp`
2. Open `scanner.py` and add your wallet address to the `TARGET_ADDRESS` variable.
3. Run the script: `python scanner.py`

## Requirements
- Python 3.9+
- Web3.py
- aiohttp
