import pandas as pd


def calculate_kpis(df: pd.DataFrame):

    df = df.copy()

    df["Order Date"] = pd.to_datetime(df["Order Date"])

   

    total_sales = df["Sales"].sum()
    total_profit = df["Profit"].sum()
    total_orders = df["Order ID"].nunique()
    customers = df["Customer ID"].nunique()
    products = df["Product ID"].nunique()
    quantity = int(df["Quantity"].sum())
    avg_discount = round(df["Discount"].mean() * 100, 2)

   
    # Monthly Data

    monthly = (
        df.groupby(df["Order Date"].dt.to_period("M"))
        .agg(
            Sales=("Sales", "sum"),
            Profit=("Profit", "sum"),
            Orders=("Order ID", "nunique"),
            Customers=("Customer ID", "nunique"),
            Products=("Product ID", "nunique"),
            Quantity=("Quantity", "sum"),
            Discount=("Discount", "mean"),
        )
    )

    if len(monthly) >= 2:

        current = monthly.iloc[-1]
        previous = monthly.iloc[-2]

        print("Montyly Table")
        print(monthly)

        print("Current Month")
        print(current)

        print("Previous Month")
        print(previous)

        def growth(curr, prev):

            if prev == 0:
                return 0

            return round(((curr - prev) / prev) * 100, 1)

        sales_delta = growth(current["Sales"], previous["Sales"])
        profit_delta = growth(current["Profit"], previous["Profit"])
        orders_delta = growth(current["Orders"], previous["Orders"])
        customers_delta = growth(current["Customers"], previous["Customers"])
        products_delta = growth(current["Products"], previous["Products"])
        quantity_delta = growth(current["Quantity"], previous["Quantity"])
        discount_delta = growth(current["Discount"], previous["Discount"])

    else:

        sales_delta = 0
        profit_delta = 0
        orders_delta = 0
        customers_delta = 0
        products_delta = 0
        quantity_delta = 0
        discount_delta = 0

    return {

        "total_sales": round(total_sales, 2),
        "total_profit": round(total_profit, 2),
        "total_orders": total_orders,
        "customers": customers,
        "products": products,
        "quantity": quantity,
        "avg_discount": avg_discount,

        "sales_delta": sales_delta,
        "profit_delta": profit_delta,
        "orders_delta": orders_delta,
        "customers_delta": customers_delta,
        "products_delta": products_delta,
        "quantity_delta": quantity_delta,
        "discount_delta": discount_delta,

    }


def format_money(value):

    if value >= 1_000_000:
        return f"${value/1_000_000:.2f} M"

    if value >= 1_000:
        return f"${value/1_000:.2f} K"

    return f"${value:.2f}"