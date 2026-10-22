# Etsy API definitions (selected)

This is a small subset of Etsy's own clarifications.

## Listing `state` values (ShopListing endpoints)

- `active`: currently active listing with quantity and not expired
- `inactive` / `edit`: no longer active, ready for modifications
- `sold_out`: once active but no available quantity
- `draft`: created but not promoted to active
- `expired`: once active, reached ending date and not auto-renewed

## Money object

A money object represents a price in a specific currency:

- `amount`: base amount in minor units (e.g., pennies)
- `divisor`: divisor to convert minor units to major currency units (e.g., 100)
- `currency_code`: 3-letter currency code (e.g., USD, CAD)

## Receipt / order status

Receipts (orders) can have statuses such as:

- `open`: created but payment not submitted (legacy)
- `paid`: created and paid, ready for shipping
- `completed`: shipped and complete
- `payment processing`: payment submitted but not fully processed
- `canceled`: canceled order
