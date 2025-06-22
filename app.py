import requests

BASE_URL = "https://zenoapi.com/api/payments"
API_KEY = "YOUR_API_KEY"  # Replace with your actual API key

HEADERS = {
    "x-api-key": API_KEY,
    "Content-Type": "application/json"
}

def create_cardholder(data):
    url = f"{BASE_URL}/cardholders/"
    response = requests.post(url, headers=HEADERS, json=data)
    return response.json()

def list_cardholders():
    url = f"{BASE_URL}/my_cardholders/"
    response = requests.get(url, headers={"x-api-key": API_KEY})
    return response.json()

def get_cardholder_by_id(cardholder_id):
    url = f"{BASE_URL}/my_cardholders_byId/{cardholder_id}/"
    response = requests.get(url, headers={"x-api-key": API_KEY})
    return response.json()

# --- Example usage ---

if __name__ == "__main__":
    # Example cardholder data
    new_cardholder = {
        "firstName": "Jumlpanji",
        "lastName": "Komplba",
        "email": "customer@mail.com",
        "phone": "+255652534449389",
        "dateOfBirth": "1990-02-28",
        "gender": "MALE",
        "address": "Sinza Mori",
        "city": "Dar es salaam",
        "state": "Dar es salaam",
        "zipCode": "12345",
        "country": "TZ",
        "documentType": "NATIONAL_ID"
    }

    # Create cardholder
    print("Creating cardholder...")
    created = create_cardholder(new_cardholder)
    print(created)

    # List all cardholders
    print("\nListing all cardholders...")
    all_cardholders = list_cardholders()
    print(all_cardholders)

    # Get a cardholder by ID (use a real cardholder_id from above response)
    if "cardholderId" in created:
        cardholder_id = created["cardholderId"]
        print(f"\nFetching cardholder by ID: {cardholder_id}")
        single_cardholder = get_cardholder_by_id(cardholder_id)
        print(single_cardholder)
