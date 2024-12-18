import requests

def requests_username_freeapi():
    url = "https://catfact.ninja/fact"
    response = requests.get(url)
    data = response.json()
    # print("data")
    if data:
        fact = data["fact"]
        length = data["length"]
        return fact, length
    else:
        raise Exception("Failed to fetch user data")
    # if data["success"] and "data" in data:
    #     user_data = data["data"]
    #     username = user_data["login"]["username"]
    #     country = user_data["location"]["country"]
    #     return username, country
    # else:
    #     raise Exception("Failed to fetch user data")

def main():
    try:
        fact, length = requests_username_freeapi()
        # print(f"Username: {username} \nCountry: {country}")
        print(f"Cat: {fact} \nSize: {length}")
    except Exception as e:
        print(str(e))
if __name__ == "__main__":
    main()