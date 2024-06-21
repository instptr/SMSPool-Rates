import requests
import os
from colorama import Fore, Back, Style, init
from dotenv import load_dotenv

init(autoreset=True)
load_dotenv()

class ServiceManager:
    def __init__(self):
        self.baseUrl = "https://api.smspool.net"

    def getServices(self):
        print(Fore.LIGHTYELLOW_EX + "[*] Retrieving services..." + Style.RESET_ALL)

        response = requests.post(f'{self.baseUrl}/service/retrieve_all')

        if response.status_code != 200:
            print(Fore.LIGHTRED_EX + "[-] Failed to retrieve services." + Style.RESET_ALL)

        return response.json()

    def getCountries(self):
        print(Fore.LIGHTYELLOW_EX + "[*] Retrieving countries..." + Style.RESET_ALL)

        response = requests.post(f'{self.baseUrl}/country/retrieve_all')

        if response.status_code != 200:
            print(Fore.LIGHTRED_EX + "[-] Failed to retrieve countries." + Style.RESET_ALL)

        return response.json()

    def findServiceId(self, services, serviceName):
        print(Fore.LIGHTYELLOW_EX + f"[*] Searching for service ID for service name: {serviceName}" + Style.RESET_ALL)

        for service in services:
            if service['name'].lower() == serviceName.lower():
                print(Fore.LIGHTGREEN_EX + Back.BLACK + f"[+] Service ID found: {service['ID']}" + Style.RESET_ALL)
                return service['ID']
            
        print(Fore.LIGHTRED_EX + "[-] Service not found." + Style.RESET_ALL)
        return None

    def checkPrice(self, serviceId, countryId, serviceName, countryName):
        global APIKEY

        print(Fore.LIGHTYELLOW_EX + f"[*] Checking price -> {serviceName} in -> {countryName}..." + Style.RESET_ALL)

        url = f'{self.baseUrl}/request/price'
        data = {
            'key': APIKEY,
            'service': serviceId,
            'country': countryId
        }

        response = requests.post(url, data=data)

        if response.status_code != 200:
            print(Fore.LIGHTRED_EX + "[-] Failed to retrieve price." + Style.RESET_ALL)

        return response.json()

class PriceFinder:
    def __init__(self):
        self.serviceManager = ServiceManager()

    def findCheapest(self):
        serviceName = input("Service Name: ")
        services = self.serviceManager.getServices()
        serviceId = self.serviceManager.findServiceId(services, serviceName)

        if serviceId is None:
            return

        countries = self.serviceManager.getCountries()
        prices = []

        totalCountries = len(countries)
        for index, country in enumerate(countries, start=1):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.LIGHTYELLOW_EX + f"Checking prices [{index}/{totalCountries}]..." + Style.RESET_ALL)

            countryId = country['ID']
            countryName = country['name']
            priceInfo = self.serviceManager.checkPrice(serviceId, countryId, serviceName, countryName)

            if isinstance(priceInfo, dict) and 'price' in priceInfo:
                price = float(priceInfo['price'])
                prices.append((price, countryName))

        prices.sort()
        cheapestPrices = prices[:3]

        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.LIGHTCYAN_EX + f"Cheapest prices for '{serviceName}':" + Style.RESET_ALL)
        for price, countryName in cheapestPrices:
            print(Fore.LIGHTGREEN_EX + f"- {countryName}: ${price:.2f}" + Style.RESET_ALL)


if __name__ == "__main__":
    APIKEY = os.getenv('API_KEY') # .env

    if APIKEY:
        priceFinder = PriceFinder()
        priceFinder.findCheapest()
    else:
        print(Fore.LIGHTRED_EX + "[!] API KEY NOT SET" + Style.RESET_ALL)
