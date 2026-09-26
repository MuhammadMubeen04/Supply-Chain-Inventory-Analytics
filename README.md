# 📦 Supply Chain & Inventory Analytics

End-to-end Data Analytics project that transforms inventory, purchase order, and demand data into actionable logistics insights using **SQL**, **Python**, and **Power BI**.

---

## 📌 Project Overview

This project analyzes 120 SKUs across multi-warehouse locations (Riyadh, Jeddah, Dammam), 400 purchase orders, and monthly demand to answer key business questions related to stock health, stock-outs, inventory value, supplier performance, lead times, and reorder priority.

The complete pipeline follows a real-world data analyst workflow:

**SQL → Python (Pandas + Matplotlib) → Power BI Dashboard**

Framed for **e-commerce / retail logistics** operations supporting multi-city inventory and supplier decisions.

---

## 🛠️ Tools & Technologies

- **SQL (MySQL)** – Data extraction and supply chain analysis
- **Python** – Data cleaning, exploratory data analysis (EDA), and visualization
- **Pandas & NumPy** – Data manipulation
- **Matplotlib & Seaborn** – Charts and visual insights
- **Power BI** – Interactive Supply Chain Dashboard
- **Git & GitHub** – Version control and project showcase

---

## ✨ Key Features

- Overall KPIs (Total SKUs, Inventory Value, Stock-out Rate, On-Time %)
- Stock status breakdown (Healthy / Low Stock / Stock-out)
- Inventory value by category and warehouse
- Supplier on-time delivery and average lead time
- Fill rate and order value by supplier
- Reorder / at-risk product list
- Interactive Power BI Dashboard with actionable recommendations

---

## 📈 Key Insights

- A meaningful share of SKUs are stock-out or below reorder point
- Inventory value concentrates in specific categories and warehouses
- Supplier on-time performance and lead times vary clearly across partners
- Reorder priority should focus on stock-outs with ongoing demand
- Balancing stock across Riyadh, Jeddah, and Dammam can reduce regional risk
- Weekly stock-out reviews and supplier scorecards support operational decisions

---

## 📁 Project Structure

```
Supply-Chain-Inventory-Analytics/
├── data/
│   ├── inventory.csv
│   ├── purchase_orders.csv
│   ├── demand.csv
│   ├── products.csv
│   └── summaries/
├── sql/
│   ├── 01_schema_and_load.sql
│   └── 02_analysis_queries.sql
├── python/
│   ├── 01_supply_chain_analysis.py
│   └── charts/
├── powerbi/
│   └── Supply_Chain_Inventory_Analytics_Dashboard.pbix
├── docs/
│   └── PowerBI_Dashboard_Guide.md
├── images/
│   ├── sql/
│   ├── python/
│   └── powerbi/
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run the Project

### 1. SQL Analysis (MySQL)
- Create the database and tables using `sql/01_schema_and_load.sql`
- Import `data/inventory.csv`, `data/purchase_orders.csv`, and `data/demand.csv`
- Run the analysis queries from `sql/02_analysis_queries.sql`

### 2. Python Analysis
```bash
pip install -r requirements.txt
python python/01_supply_chain_analysis.py
```

### 3. Power BI Dashboard
- Open `powerbi/Supply_Chain_Inventory_Analytics_Dashboard.pbix` in Power BI Desktop
- Or follow the step-by-step guide in `docs/PowerBI_Dashboard_Guide.md`

---

## 📊 Dashboard Pages (Power BI)

1. **Executive Overview** – KPIs, stock status, inventory value by category  
2. **Inventory & Products** – Warehouse performance, reorder list, top value SKUs  
3. **Suppliers** – On-time delivery, lead time, order value, fill rate  
4. **Recommendations** – Reorder priority, warehouse focus, supplier actions  

---

## 🖼️ Screenshots

### Power BI Dashboard
![Executive Overview](images/powerbi/01_executive_overview.png)
![Inventory & Products](images/powerbi/02_inventory_products.png)
![Suppliers](images/powerbi/03_suppliers.png)
![Recommendations](images/powerbi/04_recommendations.png)

### SQL Analysis
![Overall KPIs](images/sql/01_overall_kpis.png)
![Stock Status](images/sql/02_stock_status.png)
![Inventory by Category](images/sql/03_inventory_by_category.png)
![Inventory by Warehouse](images/sql/04_inventory_by_warehouse.png)
![Supplier Performance](images/sql/05_supplier_performance.png)
![Reorder List](images/sql/06_reorder_list.png)

### Python Visualizations
![Stock Status](images/python/01_stock_status.png)
![Inventory by Category](images/python/02_inventory_by_category.png)
![Inventory by Warehouse](images/python/03_inventory_by_warehouse.png)
![Supplier On-Time](images/python/04_supplier_ontime.png)
![Supplier Lead Time](images/python/05_supplier_leadtime.png)
![Top Inventory Value](images/python/07_top_inventory_value.png)

---

## 👤 Author

**Mubeen Salman**  
Aspiring Data Analyst  

- LinkedIn: [https://www.linkedin.com/in/mubeen-salman-459776364/]  
- GitHub: [https://github.com/MuhammadMubeen04]  

---

## 📄 License

This project is for educational and portfolio purposes.
