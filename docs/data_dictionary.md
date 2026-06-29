# Data Dictionary

This document describes the structure of the retail transaction dataset processed by the Retail Data Platform.

| Column | Type | Description |
|--------|------|-------------|
| transaction_id | String | Unique identifier for a retail transaction. |
| order_timestamp | DateTime | Timestamp when the transaction was completed. |
| store_id | String | Identifier of the retail store. |
| customer_id | String | Unique customer identifier. |
| product_sku | String | Product stock keeping unit (SKU). |
| quantity | Integer | Number of units purchased. |
| unit_price | Decimal | Price per unit before discounts. |
| discount_pct | Decimal | Discount percentage applied to the transaction. |
| payment_method | String | Payment method (Card, Cash, UPI, Wallet). |
| region | String | Sales region (North, South, East, West). |

## Business Rules

- `transaction_id` must be unique.
- `quantity` must be greater than zero.
- `unit_price` cannot be negative.
- `discount_pct` must be between 0 and 100.
- `payment_method` must be one of: Card, Cash, UPI, Wallet.
- `region` must be one of: North, South, East, West.