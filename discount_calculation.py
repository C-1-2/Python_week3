def calculate_discount(price, discount_percent):
    """
    This function calculates the final price after applying the discount.
    If the discount is 20% or higher, the discount is applied. 
    Otherwise, the original price is returned.
    """
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        return price

# Prompt the user to enter the original price and discount percentage
try:
    original_price = float(input("Enter the original price of the item: $"))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate the final price using the calculate_discount function
    final_price = calculate_discount(original_price, discount_percent)

    # Print the final price
    if final_price == original_price:
        print(f"No discount applied. The original price is: ${final_price:.2f}")
    else:
        print(f"After applying the discount, the final price is: ${final_price:.2f}")
except ValueError:
    print("Please enter valid numbers for the price and discount percentage.")
