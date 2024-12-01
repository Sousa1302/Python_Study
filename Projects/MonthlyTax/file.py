allProductNames = []
allProductPrices = []
allProductQuantity = []


def menu():
    while True:

        print("1. Sell Product \n2. Show Products \n3. Exit")
        option = int(input("What do you wish to do: "))
        print("\n")
        
        if option == 1:
            getProduct()
            print("\n")
        elif option == 2:
            showProducts()
            print("\n")
        elif option == 3:
            break
        else:
            print("You must type a valid option !\n")
            break


def getProduct():
    nameProduct = input("Name of Product: ")
    priceProduct = input("Price of Product: ")
    quantityProduct = input("Quantity of Product: ")

    allProductNames.append(nameProduct)
    allProductPrices.append(priceProduct)
    allProductQuantity.append(quantityProduct)


def showProducts():
    if len(allProductNames) == 0:
        print("You must enter a product first !")
    
    else:
        print("Name ; Price ; Quantity")
        for i in range(len(allProductNames)): 
            print(f"{allProductNames[i]} ; {allProductPrices[i]} ; {allProductQuantity[i]}")
        

def main():
    menu()

if __name__ == "__main__":
    main()