from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

# Setup the Chrome driver
driver = webdriver.Chrome()

# Loop through pages 1 to 4
data = []
for i in range(1, 6):
    # Correctly format the URL to navigate to each page
    driver.get(f"https://coinmarketcap.com/?page={i}")
    
    # Let the page load
    time.sleep(3)
    
    
    crypto_names = driver.find_elements(By.XPATH, "//p[@class='sc-71024e3e-0 OqPKt coin-item-symbol']")
    price = driver.find_elements(By.XPATH, "//div[@class='sc-b3fc6b7-0 dzgUIj']")
    market_cap = driver.find_elements(By.XPATH, "//span[@class='sc-11478e5d-1 jfwGHx']")
    Volume_24_hours = driver.find_elements(By.XPATH, "//p[@class='sc-71024e3e-0 bbHOdE font_weight_500']")
    Circulating_supply = driver.find_elements(By.XPATH, "//p[@class='sc-71024e3e-0 hhmVNu']")
    
    for each_name, each_price, each_market_cap, each_24hour, each_circulating in zip(crypto_names, price, market_cap, Volume_24_hours, Circulating_supply):
        data.append([each_name.text, each_price.text, each_market_cap.text, each_24hour.text, each_circulating.text])
    
    time.sleep(3)

# Close the browser after scraping
driver.close()

# Write the data to a CSV file
with open('CoinMarketCap.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Name", "Price", "Market_Cap", "Volume(24H)", "Circulating Supply"])
    writer.writerows(data)

print("Data should be written now")



























