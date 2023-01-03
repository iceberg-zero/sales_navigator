#%%

from playwright.async_api import async_playwright
import time, requests

start=time.time()
account= 'aospinad'

async def get_headers(account):
    async with async_playwright() as p:
        target_url= f"https://onlyfans.com/api2/v2/users/{account}"
        initiator_url = f"https://onlyfans.com/{account}"
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        async with page.expect_request(target_url) as target_response:
            await page.goto(initiator_url)
            target_request = await target_response.value
            init_page_headers= await target_request.all_headers()
            return(init_page_headers)

headers = await get_headers(account)
response = requests.get(f"https://onlyfans.com/api2/v2/users/{account}"
    ,headers=headers
    ,verify=False)
data = response.json()
display(data)

print(round(time.time()-start,2),"seconds")