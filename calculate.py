from steam_community_market import Market, AppID

# while True:
#     dmarket_without_tax = float(input("Enter the dmarket price: "))
#     dmarket_with_tax = 1.13 * dmarket_without_tax
#     steam_before_tax =  float(input("Enter the steam price: "))
#     steam_after_tax = 0.86 * steam_before_tax
#     profit = ((steam_after_tax-(dmarket_with_tax*99))/steam_after_tax)

#     print("-------------------------------------")
#     print(f"You'll be paying {round(dmarket_with_tax*99, 2)} on dmarket and getting {round(steam_after_tax, 2)} in the wallet")
#     print(f"Profit margin = {round(profit*100, 2)}%")
#     print("-------------------------------------")

#     option = str(input("Wanna check more stuff? "))
#     if option in ['N', 'n']:
#         break

market = Market("USD")
while True:
    item = str(input("Enter exact name of the item: "))
    dmarket_without_tax = float(input("Enter the dmarket price: "))
    dmarket_with_tax = 1.13 * dmarket_without_tax
    try:
        steam_before_tax = market.get_lowest_price(item.strip(), AppID.CSGO)
        steam_after_tax = 0.86 * steam_before_tax
        
        profit = ((steam_after_tax-dmarket_with_tax)/steam_after_tax)

        print("---------------------------------------------------------------------------------------------------------------")
        print(f"You'll be paying {round(dmarket_with_tax, 2)}$ on dmarket and getting {round(steam_after_tax, 2)}$ in the wallet")
        print(f"Profit margin = {round(profit*100, 2)}%")
        print("---------------------------------------------------------------------------------------------------------------")
    except:
        print("**********Error occurred while fetching price from the market**********")
        steam_before_tax =  float(input("Enter the price manually: "))
        steam_after_tax = 0.86 * steam_before_tax
        profit = ((steam_after_tax-(dmarket_with_tax*99))/steam_after_tax)

        print("-------------------------------------")
        print(f"You'll be paying {round(dmarket_with_tax, 2)}$ on dmarket and getting {round(steam_after_tax/99, 2)}$ in the wallet")
        print(f"Profit margin = {round(profit*100, 2)}%")
        print("-------------------------------------")


    option = str(input("Wanna check more stuff?(y/n) "))
    if option in ['N', 'n']:
        break