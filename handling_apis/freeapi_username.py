import requests

def fetch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url, timeout=10)
    response.raise_for_status()          
    data = response.json()              

    if data.get("success") and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        return username
    return None



def main():
    try:
        username = fetch_random_user_freeapi()
        if username:
            print(f"Random Username from FreeAPI: {username}")
        else:
            print("Failed to get username from FreeAPI.")
    except requests.RequestException as e:
        print(f"An error occurred while fetching data: {e}")
        
if __name__ == "__main__":
    main()