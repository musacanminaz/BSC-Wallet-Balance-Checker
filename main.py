from web3 import Web3

# Set up the web3 provider for Binance Smart Chain
provider = Web3.HTTPProvider('https://bsc-dataseed1.binance.org:443')
web3 = Web3(provider)

# Function to check BNB balance of an address
def check_bnb_balance(address):
    try:
        balance = web3.eth.get_balance(address)
        return web3.from_wei(balance, 'ether')
    except Exception as e:
        print(f"Failed to check balance for address {address}: {str(e)}")
        return None

# Read addresses from a text file
def read_addresses_from_file(file_path):
    with open(file_path, 'r') as file:
        addresses = [line.strip() for line in file]
    return addresses

def add_line_to_file(file_path, line):
    with open(file_path, 'a') as file:
        file.write(line + '\n')

# Main function
def main():
    file_path = 'addresses.txt'  # Specify the path to your text file here

    addresses = read_addresses_from_file(file_path)
    print(f"Total addresses to check: {len(addresses)}")

    for address in addresses:
        _tempadress = Web3.to_checksum_address(address.lower())
        balance = check_bnb_balance(_tempadress)
        if balance > 0:
            # Add to output file if address has balance
            add_line_to_file('output.txt', f"{address} = {balance} BNB")
            print(f"{address} = {balance} BNB")

# Run the script
main()
