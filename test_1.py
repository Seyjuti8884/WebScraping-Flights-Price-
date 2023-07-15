import time
import json
import csv
import pandas
import pandas as pd

from add_mod import *
url='https://www.makemytrip.com/flight/search?itinerary=DEL-BLR-07/07/2023&tripType=O&paxType=A-1_C-0_I-0&intl=false&cabinClass=E&ccde=IN&lang=eng'
#driver=driver.get(url)

try:
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@class='button buttonSecondry buttonBig fontSize12 relative']")))
except Exception:
    print("Website is slow")
try:
    find_cross=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@class='button buttonSecondry buttonBig fontSize12 relative']")))
    if find_cross:
        find_cross.click()
    else:
        raise Exception
except Exception:
    print("Element not found")


List1 = []

def fetch(driver):
    fields = driver.find_elements(By.XPATH, "//div[@class='makeFlex spaceBetween']")
    for field in fields:
        airline_name = field.find_element(By.XPATH, ".//div/p[@class='boldFont blackText airlineName']").text
        flight_number = field.find_element(By.XPATH, ".//div/p[@class='fliCode']").text
        default_location="Delhi to Bangalore"
        price=field.find_element(By.XPATH,".//div[@class='blackText fontSize18 blackFont white-space-no-wrap']").text
        time=field.find_element(By.XPATH,".//div[@class='stop-info flexOne']/p[1]").text
        direct=field.find_element(By.XPATH,".//p[@class='flightsLayoverInfo']").text
        direct_or_not=''
        if direct=='Non stop':
            direct_or_not=direct_or_not+'Non stop'
        else:
            direct_or_not=direct_or_not+'Lay over in india'

        #flight_info = f'{default_location} : {airline_name} - {flight_number} - {price} - {time} - {direct_or_not}'
        flight_info={
            "Origin_location to Destination_location":default_location,
            "Airline_Name":airline_name,
            "Airline_number":flight_number,
            "Ticket Cost":price,
            "Timing":time,
            "Direct or Layover":direct_or_not

        }
        List1.append(flight_info)


# Example usage:
fetch(driver)
with open("Make_my_trip_scraped_data.json", "w") as write_file:
    json.dump(List1, write_file, indent=4)


df=pd.read_json('Make_my_trip_scraped_data.json')
df.to_csv('flight_data.csv')