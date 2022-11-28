from requests import get


API_KEY = "022c790f3bad250bf978"
URL = "https://free.currconv.com/"


def receive_currency():
    endpoint = f"api/v7/currencies?apiKey={API_KEY}"
    url = URL + endpoint
    data = get(url).json()['results']
    data = list(data.items())
    data.sort()
    return data

def print_currencies(currencies):
    print("ID - NAME OF COUNTRY - CURRENCY SYMBOL")
    for name, currency in currencies:
        name = currency['currencyName']
        ID = currency['id']
        symbol = currency.get("currencySymbol", "")
        print(f"{ID} - {name} - {symbol}")


def exchange(currency1, currency2):
    endpoint = f"api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey={API_KEY}"
    url = URL + endpoint
    response = get(url)
    data = response.json()
    if(len(data)==0):
        print("You have entered invalid currencies")
        return 
    return list(data.values())[0]

def check_quit(word):
    if(word=="quit" or word=="q"):
        return True

    return False

def main():
    print("---Welcome to the Currency Converter---")
    print("To print the list of currencies, enter list")
    print("To perform a conversion, enter convert")
    run = True
    while(run):
        print("----------------------")
        val = input("Enter command: ").lower()
        if(val=="q"):
            run = False
        elif(val=="convert"):
            base_curr = input("Enter base currency: ")
            if(check_quit(base_curr)):
                run = False
            convert_curr = input("Enter the currency you wish to convert to: ")
            if(check_quit(base_curr)):
                run = False
            conversion = exchange(base_curr, convert_curr)
            print(f"{base_curr} -> {convert_curr} = {conversion}")
        elif(val=="list"):
            data  = receive_currency()
            print_currencies(data)
    print("Program has closed successfully")
    print("----------------------")

main()
            