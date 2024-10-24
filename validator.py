import requests

def check_validator_status(validator_address, blockchain_api_url):
    # Build the API URL to get validator details
    url = f"{blockchain_api_url}/validators/{validator_address}"

    try:
        # Make a request to get the validator's status
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            status = data.get("status")
            voting_power = data.get("voting_power")
            jailed = data.get("jailed")

            # Check if validator is active and not jailed
            if status == "BOND_STATUS_BONDED" and not jailed:
                print(f"Validator {validator_address} is active with {voting_power} voting power.")
            else:
                print(f"Validator {validator_address} is inactive or jailed.")
        else:
            print(f"Failed to fetch validator status. HTTP Error: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
validator_address = "cosmosvaloper1...your_validator_address"
blockchain_api_url = "https://blockchain-api.com"  # Replace with actual API endpoint

check_validator_status(validator_address, blockchain_api_url)
