import requests
url1="https://api.zippopotam.us/us/33162"
try:
    response = requests.get(url1)
    print(response)
    print(response.status_code)
    if response.status_code == 200:
        data = response.json()
        print("maininfo:",data)
        print("first:",data["places"])
        # print("second:",data["postcode"])
        print("thired:",data["country"])
        mainone=data["places"]
        print(mainone)
        for r in mainone:
            for k,v in r.items():
                print('items:',k, v) 
        
        for each_list_element in mainone:
            for key,value in each_list_element.items():
                print("doesnotchange:",key,"wecanchange:",value)

          
        display("Success! status:",response.status_code)
    else:
        print("Error:",response.status_code)
except Exception as e:
    print("Error:",e)