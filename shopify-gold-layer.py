from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()

# --- Gold 1: Revenue by Month ---
spark.sql("""
    CREATE OR REPLACE TABLE gold_revenue_by_month AS
    SELECT
        year,
        month,
        COUNT(DISTINCT order_id)          AS total_orders,
        SUM(quantity)                     AS total_units,
        ROUND(SUM(revenue), 2)            AS total_revenue,
        ROUND(SUM(profit),  2)            AS total_profit,
        ROUND(AVG(processing_days), 1)    AS avg_processing_days
    FROM silver_shopify_orders
    GROUP BY year, month
    ORDER BY year, month
""")
print(" gold_revenue_by_month done")

# --- Gold 2: Revenue by Segment ---
spark.sql("""
    CREATE OR REPLACE TABLE gold_revenue_by_segment AS
    SELECT
        segment,
        year,
        COUNT(DISTINCT order_id)          AS total_orders,
        ROUND(SUM(revenue), 2)            AS total_revenue,
        ROUND(SUM(profit),  2)            AS total_profit,
        ROUND(AVG(quantity), 2)           AS avg_units_per_order
    FROM silver_shopify_orders
    GROUP BY segment, year
    ORDER BY year, total_revenue DESC
""")
print("gold_revenue_by_segment done")

# --- Gold 3: Order Priority Summary ---
spark.sql("""
    CREATE OR REPLACE TABLE gold_order_priority AS
    SELECT
        order_priority,
        COUNT(DISTINCT order_id)          AS total_orders,
        ROUND(SUM(revenue), 2)            AS total_revenue,
        ROUND(SUM(profit),  2)            AS total_profit
    FROM silver_shopify_orders
    GROUP BY order_priority
    ORDER BY total_profit DESC
""")
print("gold_order_priority done")

# --- Preview all 3 ---
print("\n Revenue by Month:")
display(spark.table("gold_revenue_by_month"))

print("\n Revenue by Segment:")
display(spark.table("gold_revenue_by_segment"))

print("\n Order Priority:")
display(spark.table("gold_order_priority"))
