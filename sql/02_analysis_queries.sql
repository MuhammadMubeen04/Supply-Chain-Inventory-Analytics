-- Supply Chain & Inventory - Key SQL Queries
USE supply_chain_analytics;

-- 1. OVERALL KPIs
SELECT 
    COUNT(*) AS total_skus,
    SUM(OnHandQty) AS total_units_on_hand,
    ROUND(SUM(InventoryValue), 2) AS total_inventory_value,
    SUM(CASE WHEN StockStatus = 'Stock-out' THEN 1 ELSE 0 END) AS stockout_skus,
    SUM(CASE WHEN StockStatus = 'Low Stock' THEN 1 ELSE 0 END) AS low_stock_skus,
    ROUND(SUM(CASE WHEN StockStatus = 'Stock-out' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 1) AS stockout_rate_pct
FROM inventory;

-- 2. STOCK STATUS BREAKDOWN
SELECT StockStatus, COUNT(*) AS skus, SUM(OnHandQty) AS units, ROUND(SUM(InventoryValue), 2) AS value
FROM inventory
GROUP BY StockStatus
ORDER BY skus DESC;

-- 3. INVENTORY BY CATEGORY
SELECT Category,
       COUNT(*) AS skus,
       SUM(OnHandQty) AS units,
       ROUND(SUM(InventoryValue), 2) AS inventory_value,
       SUM(CASE WHEN StockStatus = 'Stock-out' THEN 1 ELSE 0 END) AS stockouts
FROM inventory
GROUP BY Category
ORDER BY inventory_value DESC;

-- 4. INVENTORY BY WAREHOUSE
SELECT Warehouse,
       COUNT(*) AS skus,
       SUM(OnHandQty) AS units,
       ROUND(SUM(InventoryValue), 2) AS inventory_value,
       SUM(CASE WHEN StockStatus = 'Stock-out' THEN 1 ELSE 0 END) AS stockouts
FROM inventory
GROUP BY Warehouse
ORDER BY inventory_value DESC;

-- 5. SUPPLIER PERFORMANCE
SELECT SupplierName,
       COUNT(*) AS orders,
       ROUND(AVG(LeadTimeDays), 1) AS avg_lead_time_days,
       ROUND(AVG(OnTime) * 100, 1) AS on_time_pct,
       ROUND(AVG(FillRate) * 100, 1) AS avg_fill_rate_pct,
       ROUND(SUM(OrderValue), 2) AS total_order_value
FROM purchase_orders
GROUP BY SupplierName
ORDER BY on_time_pct DESC;

-- 6. LOW STOCK / REORDER LIST
SELECT ProductID, ProductName, Category, Warehouse, OnHandQty, ReorderPoint, StockStatus, InventoryValue
FROM inventory
WHERE StockStatus IN ('Stock-out', 'Low Stock')
ORDER BY StockStatus, OnHandQty;

-- 7. TOP PRODUCTS BY INVENTORY VALUE
SELECT ProductID, ProductName, Category, OnHandQty, InventoryValue, StockStatus
FROM inventory
ORDER BY InventoryValue DESC
LIMIT 15;

-- 8. DEMAND VS STOCK (join sample)
SELECT i.ProductID, i.ProductName, i.OnHandQty, i.ReorderPoint, i.StockStatus,
       ROUND(AVG(d.UnitsSold), 1) AS avg_monthly_demand
FROM inventory i
LEFT JOIN demand d ON i.ProductID = d.ProductID
GROUP BY i.ProductID, i.ProductName, i.OnHandQty, i.ReorderPoint, i.StockStatus
ORDER BY avg_monthly_demand DESC
LIMIT 20;
