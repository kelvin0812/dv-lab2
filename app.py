import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Lesson 5: complete coffee app
data = {
    'Coffee Type': ['Espresso', 'Latte', 'Cappuccino', 'Americano', 'Mocha'],
    'Sales': [350, 450, 550, 300, 150],
}
df = pd.DataFrame(data)

best_sale = df[df["Sales"] == df["Sales"].max()]
worst_sale = df[df["Sales"] == df["Sales"].min()]

st.title("XYZ Coffee Shop Sales Analysis")

st.subheader("Bar Chart of Coffee Sales")
fig, ax = plt.subplots()
ax.bar(df["Coffee Type"], df["Sales"], color="skyblue")
ax.bar(best_sale["Coffee Type"], best_sale["Sales"], color="green", label="Best Sale")
ax.bar(worst_sale["Coffee Type"], worst_sale["Sales"], color="red", label="Worst Sale")
ax.set_xlabel("Coffee Type")
ax.set_ylabel("Sales")
ax.legend()
st.pyplot(fig)

st.subheader("Pie Chart of Coffee Sales")
fig2, ax2 = plt.subplots()
colors = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#ff6666"]
ax2.pie(df["Sales"], labels=df["Coffee Type"], autopct="%1.1f%%", startangle=90, colors=colors)
ax2.axis("equal")
st.pyplot(fig2)

st.write("### Best Sale")
st.write(best_sale)
st.write("### Worst Sale")
st.write(worst_sale)
