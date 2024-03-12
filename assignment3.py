def main():
    # Ask the user to enter the original price of an item
    original_price = float(input("Enter the original price of the item: "))

    # Ask the user to enter the discount percentage
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate and print the final price after applying the discount
    print("The discounted price is:", calculate_discount(original_price, discount_percent))

# calculate the final price after applying a discount
def calculate_discount(price, discount_percent):
    if discount_percent > 20:
        discount = price * (discount_percent / 100)
        return price - discount
    return price

main()
