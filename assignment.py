import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="XYZ Tea House Dashboard",
    page_icon="🍵",
    layout="wide",
)

# Tea sales dataset

df = pd.DataFrame(
    {
        "Tea Type": [
            "Green Tea",
            "Black Tea",
            "Oolong",
            "Jasmine",
            "Chamomile",
            "Matcha Latte",
            "Milk Tea",
            "Thai Tea",
            "Teh Tarik",
            "Bubble Tea",
        ],
        "Category": [
            "Hot",
            "Hot",
            "Hot",
            "Hot",
            "Hot",
            "Specialty",
            "Specialty",
            "Specialty",
            "Specialty",
            "Specialty",
        ],
        "Sales": [220, 310, 150, 180, 90, 410, 520, 380, 460, 600],
    }
)

st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(135deg, #f6f3ee 0%, #eef8f0 100%);
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        h1 {
            color: #2f4f3f;
            font-weight: 700;
        }
        .metric-card {
            background: rgba(255,255,255,0.7);
            border: 1px solid rgba(47,79,63,0.12);
            border-radius: 14px;
            padding: 1rem 1.2rem;
            box-shadow: 0 4px 12px rgba(0,0,0,0.04);
        }
        div[data-testid="stDataFrame"] {
            border-radius: 12px;
            overflow: hidden;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("XYZ Tea House Sales Analysis")
st.caption("A clean view of product performance by category and sales volume")

# Filters
category = st.selectbox("Product category", ["All"] + sorted(df["Category"].unique()))
filtered = df if category == "All" else df[df["Category"] == category]

min_sales = st.slider(
    "Minimum sales threshold",
    min_value=int(df["Sales"].min()),
    max_value=int(df["Sales"].max()),
    value=int(df["Sales"].min()),
    step=10,
)
filtered = filtered[filtered["Sales"] >= min_sales]

if filtered.empty:
    st.warning("No teas match the current filters.")
    st.stop()

best_sale = filtered.loc[filtered["Sales"].idxmax()]
worst_sale = filtered.loc[filtered["Sales"].idxmin()]

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown(f"<div class='metric-card'><h4>Total Sales</h4><h2>${filtered['Sales'].sum():,.0f}</h2></div>", unsafe_allow_html=True)
with col2:
    st.markdown(f"<div class='metric-card'><h4>Average Sale</h4><h2>${filtered['Sales'].mean():,.0f}</h2></div>", unsafe_allow_html=True)
with col3:
    st.markdown(f"<div class='metric-card'><h4>Best Seller</h4><h3>{best_sale['Tea Type']}</h3></div>", unsafe_allow_html=True)
with col4:
    st.markdown(f"<div class='metric-card'><h4>Products Shown</h4><h2>{len(filtered)}</h2></div>", unsafe_allow_html=True)

st.subheader("Tea sales data")
formatted = filtered.copy()
formatted["Sales"] = formatted["Sales"].map(lambda value: f"${value:,.0f}")
st.dataframe(formatted, use_container_width=True, hide_index=True)

left_col, right_col = st.columns(2)

with left_col:
    st.subheader("Bar chart of tea sales")
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(filtered["Tea Type"], filtered["Sales"], color="#8ecae6")
    ax.bar(best_sale["Tea Type"], best_sale["Sales"], color="#2a9d8f", label="Best Sale")
    ax.bar(worst_sale["Tea Type"], worst_sale["Sales"], color="#e76f51", label="Lowest Sale")
    ax.set_xlabel("Tea Type")
    ax.set_ylabel("Sales")
    ax.tick_params(axis="x", rotation=45)
    ax.grid(axis="y", linestyle="--", alpha=0.3)
    ax.legend(frameon=False)
    st.pyplot(fig)

with right_col:
    st.subheader("Sales mix")
    fig2, ax2 = plt.subplots(figsize=(8, 5))
    ax2.pie(
        filtered["Sales"],
        labels=filtered["Tea Type"],
        autopct="%1.1f%%",
        startangle=90,
        wedgeprops={"edgecolor": "white", "linewidth": 1},
        colors=["#a8dadc", "#82c7b8", "#f4d35e", "#f7a072", "#8ecae6", "#90be6d"],
    )
    ax2.axis("equal")
    st.pyplot(fig2)

st.subheader("Highlights")
col_a, col_b = st.columns(2)

with col_a:
    st.markdown("### Best seller")
    st.dataframe(best_sale.to_frame().T, use_container_width=True, hide_index=True)

with col_b:
    st.markdown("### Lowest seller")
    st.dataframe(worst_sale.to_frame().T, use_container_width=True, hide_index=True)
