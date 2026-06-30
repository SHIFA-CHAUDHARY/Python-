import requests 
import random
def fatch_random_user_freeAPIs():
    url = "https://api.freeapi.app/api/v1/public/randomproducts"
    response = requests.get(url)
    data = response.json()
    
    if data["success"] and "data" in data:
        user_data = data["data"]["data"]
        
        user_data = random.choice(user_data)
        user_price = user_data["price"]
        user_title= user_data["title"]
        
        return user_price, user_title
    
    else :
        raise Exception("Failes to fatch user data")
    
    
def main():
    try:
        user_price, user_title = fatch_random_user_freeAPIs()
        print(f"user_title : {user_title} \n user_price : {user_price}")
            
    except Exception as e:
        print(str(e))
            
            
if __name__ == "__main__":
    main()
    
          
            
            