"""Supply Chain & Inventory Analytics - EDA and charts"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

BASE = Path(__file__).parent.parent
DATA = BASE / "data"
CHARTS = Path(__file__).parent / "charts"
CHARTS.mkdir(exist_ok=True)
SUM = DATA / "summaries"
SUM.mkdir(exist_ok=True)

sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams["figure.figsize"] = (11, 6)

inv = pd.read_csv(DATA / "inventory.csv")
po = pd.read_csv(DATA / "purchase_orders.csv")
dem = pd.read_csv(DATA / "demand.csv")

print("=" * 60)
print("SUPPLY CHAIN & INVENTORY ANALYTICS")
print("=" * 60)
print(f"SKUs: {len(inv)}")
print(f"Inventory value: ${inv['InventoryValue'].sum():,.0f}")
print(f"Stock-outs: {(inv['StockStatus']=='Stock-out').sum()}")
print(f"Low stock: {(inv['StockStatus']=='Low Stock').sum()}")
print(f"PO on-time rate: {po['OnTime'].mean()*100:.1f}%")
print(f"Avg lead time: {po['LeadTimeDays'].mean():.1f} days")

# Charts
fig, ax = plt.subplots()
inv["StockStatus"].value_counts().plot.pie(autopct="%1.1f%%", ax=ax, colors=["#59a14f", "#f28e2b", "#e15759"], startangle=90)
ax.set_ylabel("")
ax.set_title("Stock Status Distribution")
plt.tight_layout()
plt.savefig(CHARTS / "01_stock_status.png", dpi=150)
plt.close()

fig, ax = plt.subplots()
inv.groupby("Category")["InventoryValue"].sum().sort_values().plot(kind="barh", color="#4e79a7", ax=ax)
ax.set_title("Inventory Value by Category")
ax.set_xlabel("Value ($)")
plt.tight_layout()
plt.savefig(CHARTS / "02_inventory_by_category.png", dpi=150)
plt.close()

fig, ax = plt.subplots()
inv.groupby("Warehouse")["InventoryValue"].sum().sort_values().plot(kind="barh", color="#76b7b2", ax=ax)
ax.set_title("Inventory Value by Warehouse")
ax.set_xlabel("Value ($)")
plt.tight_layout()
plt.savefig(CHARTS / "03_inventory_by_warehouse.png", dpi=150)
plt.close()

sup = po.groupby("SupplierName").agg(OnTimePct=("OnTime", "mean"), AvgLead=("LeadTimeDays", "mean"), Orders=("PO_ID", "count"))
sup["OnTimePct"] = (sup["OnTimePct"] * 100).round(1)
fig, ax = plt.subplots()
sup["OnTimePct"].sort_values().plot(kind="barh", color="#59a14f", ax=ax)
ax.set_title("Supplier On-Time Delivery %")
ax.set_xlabel("On-Time %")
plt.tight_layout()
plt.savefig(CHARTS / "04_supplier_ontime.png", dpi=150)
plt.close()

fig, ax = plt.subplots()
sup["AvgLead"].sort_values().plot(kind="barh", color="#f28e2b", ax=ax)
ax.set_title("Average Lead Time by Supplier (Days)")
ax.set_xlabel("Days")
plt.tight_layout()
plt.savefig(CHARTS / "05_supplier_leadtime.png", dpi=150)
plt.close()

fig, ax = plt.subplots()
status_wh = inv.groupby(["Warehouse", "StockStatus"]).size().unstack(fill_value=0)
status_wh.plot(kind="bar", stacked=True, ax=ax, color=["#59a14f", "#f28e2b", "#e15759"])
ax.set_title("Stock Status by Warehouse")
ax.tick_params(axis="x", rotation=20)
ax.legend(title="Status")
plt.tight_layout()
plt.savefig(CHARTS / "06_status_by_warehouse.png", dpi=150)
plt.close()

top_val = inv.nlargest(10, "InventoryValue")
fig, ax = plt.subplots()
ax.barh(top_val["ProductName"], top_val["InventoryValue"], color="#4e79a7")
ax.set_title("Top 10 Products by Inventory Value")
ax.set_xlabel("Value ($)")
plt.tight_layout()
plt.savefig(CHARTS / "07_top_inventory_value.png", dpi=150)
plt.close()

monthly = dem.groupby("YearMonth")["UnitsSold"].sum()
fig, ax = plt.subplots()
monthly.plot(kind="bar", color="#9c755f", ax=ax)
ax.set_title("Total Units Sold by Month")
ax.tick_params(axis="x", rotation=30)
plt.tight_layout()
plt.savefig(CHARTS / "08_monthly_demand.png", dpi=150)
plt.close()

print(f"Charts → {CHARTS}")

# Summaries
pd.DataFrame([{
    "total_skus": len(inv),
    "inventory_value": round(inv["InventoryValue"].sum(), 2),
    "stockouts": int((inv["StockStatus"]=="Stock-out").sum()),
    "low_stock": int((inv["StockStatus"]=="Low Stock").sum()),
    "ontime_pct": round(po["OnTime"].mean()*100, 1),
    "avg_lead_days": round(po["LeadTimeDays"].mean(), 1)
}]).to_csv(SUM / "overall_kpis.csv", index=False)
inv.groupby("StockStatus").size().to_csv(SUM / "stock_status.csv")
inv.groupby("Category")["InventoryValue"].sum().to_csv(SUM / "value_by_category.csv")
sup.to_csv(SUM / "supplier_performance.csv")
print("Done.")
