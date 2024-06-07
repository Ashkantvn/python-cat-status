import requests




def get_status(status_code="404"):
    request_url=f"https://http.cat/{status_code}"
    request_data= requests.get(request_url)
    return request_data




if __name__ == "__main__":
    print("---CAT STATUS CODE---")

    status_code = input("\n please enter your status code : ")
    request_data =get_status(status_code)

    print(type(request_data))
    print(request_data)
