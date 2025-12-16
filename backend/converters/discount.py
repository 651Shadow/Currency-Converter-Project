def calc_discount(price: float, discount_percent: float):
    # Calculate the discounted price given the original price and discount percentage
    
    if discount_percent < 0 or discount_percent >= 100:
        raise ValueError("Discount percent must be between 0 and 100")

    # Calculate the discount amount
    discount = (discount_percent / 100) * price
    discounted_price = price - discount

    return discounted_price


if __name__ == "__main__":
    print(calc_discount(100, 10))
    print(calc_discount(200, 25))
    print(calc_discount(50, 0))  
