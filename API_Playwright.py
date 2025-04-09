import json
from playwright.sync_api import sync_playwright
with sync_playwright()as playwright:


    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.goto("https://jsonplaceholder.typicode.com")
    url="https://jsonplaceholder.typicode.com"
    endpoint="/posts/1"
    page.wait_for_timeout(1000)
 # get request Retrieves data from the server. It does not change the state of the resource.
    response = page.request.get(f"{url}{endpoint}")
    print("status",response.status)
    print("header",response.headers)
    print("json",response.json())
    assert response.status ==200
    data1= response.json()
    print(f"Userid,{data1['userId']}")
#post request The POST method is used to send data to a server to create a new resource
    url2= "https://jsonplaceholder.typicode.com/posts"
    headers={'content-type': 'application/json; charset=utf-8', 'transfer-encoding': 'chunked'}
    payload={'userId': 2, 'id': 2, 'title': 'test'}
    response1 = page.request.post(url2, headers=headers, data=json.dumps(payload))
    print(response1.status)
    if (response1.status==201):
     print("posted sucessfully")

#put The PUT method is typically used to update an existing resource on the server
