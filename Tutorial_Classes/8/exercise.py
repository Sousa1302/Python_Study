valor_total = int(input("Your total value: "))
discounted_total = 0
discount = 0

if valor_total < 100:
    print("No discount available !")

elif valor_total >= 100 and valor_total <= 500:
    discount = (valor_total * 10) / 100
    print(f"Discount aplied: {discount}")
    discounted_total = valor_total - discount
    print(f"Your total value updated: {discounted_total}")

elif valor_total > 500:
    discount = (valor_total * 20) / 100
    print(f"Discount applied: {discount}")
    discounted_total = valor_total - discount
    print(f"Your total value updated {discounted_total}")
    

# Needs an variable amount improvement and logic improvement 
