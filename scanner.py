import asyncio
from web3 import AsyncWeb3
from web3.providers.async_rpc import AsyncHTTPProvider

# Configuration
TARGET_ADDRESS = "0x0000000000000000000000000000000000000000" # Replace with target
NETWORKS = {
    "Ethereum Mainnet": "https://cloudflare-eth.com",
    "Binance Smart Chain": "https://bsc-dataseed.binance.org/",
    "Polygon POS": "https://polygon-rpc.com",
    "Arbitrum One": "https://arb1.arbitrum.io/rpc"
}

async def get_balance(network_name, rpc_url, address):
    try:
        w3 = AsyncWeb3(AsyncHTTPProvider(rpc_url))
        # Ensure address is checksummed
        checksum_address = w3.to_checksum_address(address)
        balance_wei = await w3.eth.get_balance(checksum_address)
        balance_eth = w3.from_wei(balance_wei, 'ether')
        
        return f"[+] {network_name}: {balance_eth:.4f} Native Tokens"
    except Exception as e:
        return f"[!] {network_name}: Error - {str(e)}"

async def main():
    print(f"--- Scanning Wallet: {TARGET_ADDRESS} ---")
    
    # Create tasks for parallel execution
    tasks = [get_balance(name, url, TARGET_ADDRESS) for name, url in NETWORKS.items()]
    
    # Wait for all network scans to complete
    results = await asyncio.gather(*tasks)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    if TARGET_ADDRESS == "0x0000000000000000000000000000000000000000":
        print("Please update the TARGET_ADDRESS in scanner.py first.")
    else:
        asyncio.run(main())
