# 🏗️ Shopify Medallion Architecture — Full Pipeline

## Overview
End-to-end automated data pipeline built on Microsoft Fabric 
that ingests Shopify e-commerce orders through a Bronze/Silver/
Gold Medallion Architecture and delivers an executive Power BI 
dashboard refreshed daily.

## Architecture
Shopify REST API
↓
[Bronze] Raw ingestion → bronze_shopify_orders
↓
[Silver] Clean & transform → silver_shopify_orders
↓
[Gold] Aggregate → gold_revenue_by_month
→ gold_revenue_by_segment
→ gold_order_priority
↓
[Power BI] Shopify Executive Dashboard

## Tech Stack
| Tool | Purpose |
|---|---|
| Microsoft Fabric | Cloud data platform |
| Delta Lake | Storage format |
| PySpark | Data processing |
| Shopify REST API | Data source |
| Python | Scripting |
| Power BI | Visualisation |

## Notebooks
| Notebook | Purpose |
|---|---|
| bronze_shopify_orders | API ingestion |
| silver_shopify_orders | Transformation |
| gold_shopify_orders | Aggregation |

## Pipeline
- Orchestrated via Fabric Data Pipeline
- Runs daily at 2:00 AM WAT
- Failure alerting via email
- Incremental loading on Bronze layer

## Power BI Dashboard
- KPI Cards: Total Revenue, Total Orders, Total Profit
- Line Chart: Revenue trend by month
- Bar Chart: Revenue by customer segment
- Donut Chart: Orders by priority
- Slicer: Filter by year

## Results
- 101 Shopify orders processed end to end
- 3 Gold tables powering live dashboard
- 0 manual steps — fully automated daily refresh
- Dashboard available every morning by 3AM WAT

## Setup
1. Clone this repo
2. Import notebooks into Microsoft Fabric workspace
3. Attach LH_Landing lakehouse to all notebooks
4. Create Data Pipeline and link notebooks in sequence
5. Set schedule to daily 2AM
6. Set semantic model refresh to daily 3AM
7. Open Power BI dashboard
