def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.

    The discount is applied only if it is 20% or higher.
    Otherwise, the original price is returned.

    Args:
        price (float or int): The original price of the item.
        discount_percent (float or int): The discount percentage (e.g., 20 for 20%).

    Returns:
        float: The final price after discount, or the original price if no discount was applied.
    """
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        # Calculate the final price
        final_price = price - discount_amount
        return final_price
    else:
        # Return the original price if discount is less than 20%
        return price

# Prompt the user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage (e.g., 15, 25): "))

    # Calculate the final price using the function
    final_price_calculated = calculate_discount(original_price, discount_percentage)

    # Print the result
    if discount_percentage >= 20:
        print(f"Original Price: ${original_price:.2f}")
        print(f"Discount Applied: {discount_percentage:.2f}%")
        print(f"Final Price after discount: ${final_price_calculated:.2f}")
    else:
        print(f"Original Price: ${original_price:.2f}")
        print(f"Discount Percentage: {discount_percentage:.2f}% (No discount applied as it's less than 20%)")
        print(f"Final Price: ${final_price_calculated:.2f}")

except ValueError:
    print("Invalid input. Please enter valid numbers for price and discount percentage.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")