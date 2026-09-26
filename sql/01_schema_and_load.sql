-- Supply Chain & Inventory Analytics - MySQL Schema

CREATE DATABASE IF NOT EXISTS supply_chain_analytics;
USE supply_chain_analytics;

CREATE TABLE IF NOT EXISTS inventory (
    ProductID       VARCHAR(20),
    ProductName     VARCHAR(50),
    Category        VARCHAR(50),
    UnitCost        DECIMAL(10,2),
    UnitPrice       DECIMAL(10,2),
    ReorderPoint    INT,
    SupplierID      VARCHAR(10),
    Warehouse       VARCHAR(50),
    SupplierName    VARCHAR(100),
    OnHandQty       INT,
    InventoryValue  DECIMAL(12,2),
    StockStatus     VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS purchase_orders (
    PO_ID           VARCHAR(20),
    ProductID       VARCHAR(20),
    SupplierID      VARCHAR(10),
    SupplierName    VARCHAR(100),
    Warehouse       VARCHAR(50),
    OrderDate       DATE,
    PlannedDelivery DATE,
    ActualDelivery  DATE,
    LeadTimeDays    INT,
    OrderQty        INT,
    ReceivedQty     INT,
    OnTime          INT,
    UnitCost        DECIMAL(10,2),
    FillRate        DECIMAL(6,3),
    OrderValue      DECIMAL(12,2)
);

CREATE TABLE IF NOT EXISTS demand (
    ProductID   VARCHAR(20),
    YearMonth   VARCHAR(10),
    UnitsSold   INT
);

-- Import CSVs from data/ folder into these tables
