import pandas as pd
import plotly.express as px


def monthly_sales_chart(df, period="Monthly"):

    df = df.copy()

    df["Order Date"] = pd.to_datetime(df["Order Date"])

    if period == "Daily":

        sales = (
            df.groupby("Order Date")["Sales"]
            .sum()
            .reset_index()
        )

        title = "📅 Daily Sales Trend"

    elif period == "Weekly":

        sales = (
            df.groupby(pd.Grouper(key="Order Date", freq="W"))["Sales"]
            .sum()
            .reset_index()
        )

        title = "📆 Weekly Sales Trend"

    else:

        sales = (
            df.groupby(pd.Grouper(key="Order Date", freq="ME"))["Sales"]
            .sum()
            .reset_index()
        )

        title = "📈 Monthly Sales Trend"

    fig = px.line(
        sales,
        x="Order Date",
        y="Sales",
        markers=True,
        title=title,
        color_discrete_sequence=["#2563EB"],
    )

    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=20, r=20, t=50, b=20),
    )

    return fig


def category_sales_chart(df):

    category = (
        df.groupby("Category")["Sales"]
        .sum()
        .reset_index()
        .sort_values(by="Sales", ascending=False)
    )

    fig = px.bar(
        category,
        x="Category",
        y="Sales",
        color="Category",
        title="📦 Sales by Category",
        color_discrete_sequence=px.colors.qualitative.Set2,
    )

    fig.update_layout(
        template="plotly_white",
        height=420,
        showlegend=False,
    )

    return fig


def region_sales_chart(df):

    region = (
        df.groupby("Region")["Sales"]
        .sum()
        .reset_index()
        .sort_values(by="Sales", ascending=False)
    )

    fig = px.bar(
        region,
        x="Region",
        y="Sales",
        color="Region",
        title="🌍 Sales by Region",
        color_discrete_sequence=px.colors.qualitative.Set2,
    )

    fig.update_layout(
        template="plotly_white",
        height=420,
        showlegend=False,
    )

    return fig


def segment_chart(df):

    segment = (
        df.groupby("Segment")["Sales"]
        .sum()
        .reset_index()
    )

    fig = px.pie(
        segment,
        names="Segment",
        values="Sales",
        hole=0.55,
        title="🥧 Sales by Segment",
        color_discrete_sequence=px.colors.qualitative.Pastel,
    )

    fig.update_layout(
        template="plotly_white",
        height=420,
        showlegend=True,
    )

    return fig


def top_products_chart(df):

    products = (
        df.groupby("Product Name")["Sales"]
        .sum()
        .nlargest(10)
        .reset_index()
    )

    fig = px.bar(
        products,
        x="Sales",
        y="Product Name",
        orientation="h",
        title="🏆 Top 10 Products",
        color_discrete_sequence=px.colors.qualitative.Set2,
    )

    fig.update_layout(
        template="plotly_white",
        height=500,
        yaxis={"categoryorder": "total ascending"},
    )

    return fig


def top_customers_chart(df):

    customers = (
        df.groupby("Customer Name")["Sales"]
        .sum()
        .nlargest(10)
        .reset_index()
    )

    fig = px.bar(
        customers,
        x="Sales",
        y="Customer Name",
        orientation="h",
        title="👥 Top 10 Customers",
        color_discrete_sequence=px.colors.qualitative.Set2,
    )

    fig.update_layout(
        template="plotly_white",
        height=500,
        yaxis={"categoryorder": "total ascending"},
    )

    return fig


def profit_chart(df):

    profit = (
        df.groupby("Category")["Profit"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        profit,
        x="Category",
        y="Profit",
        color="Category",
        title="💰 Profit by Category",
        color_discrete_sequence=px.colors.qualitative.Set2,
    )

    fig.update_layout(
        template="plotly_white",
        height=420,
        showlegend=False,
    )


def top10_products(df):

    products = (
        df.groupby("Product Name")["Sales"]
        .sum()
        .nlargest(10)
        .sort_values()
        .reset_index()
    )

    fig = px.bar(
        products,
        x="Sales",
        y="Product Name",
        orientation="h",
        title="🏆 Top 10 Products",
        color_discrete_sequence=px.colors.qualitative.Set2,
    )

    fig.update_layout(
        template="plotly_white",
        height=450,
    )

    return fig


def top10_customers(df):

    customers = (
        df.groupby("Customer Name")["Sales"]
        .sum()
        .nlargest(10)
        .sort_values()
        .reset_index()
    )

    fig = px.bar(
        customers,
        x="Sales",
        y="Customer Name",
        orientation="h",
        title="👥 Top 10 Customers",
        color_discrete_sequence=px.colors.qualitative.Set2,
    )

    fig.update_layout(
        template="plotly_white",
        height=450,
    )

    return fig

def profit_trend_chart(df):

    profit = (
        df.groupby(df["Order Date"].dt.to_period("M"))["Profit"]
        .sum()
        .reset_index()
    )

    profit["Order Date"] = profit["Order Date"].astype(str)

    fig = px.line(
        profit,
        x="Order Date",
        y="Profit",
        markers=True,
        title="💰 Monthly Profit Trend",
        color_discrete_sequence=["#2563EB"],
    )

    fig.update_layout(
        template="plotly_white",
        height=420,
    )

    return fig