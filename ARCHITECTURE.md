# Reconstruction architecture

```text
Product catalogue -> cart -> server-side price validation -> order -> payment gateway verification
```

The model verifies catalogue/order logic only. It does not charge money or reconstruct the original storefront. Real checkout needs a server-side gateway order, webhook signature checks, idempotency and stock transactions.

See METHODOLOGY.md for research and evaluation details, and reconstruction/model.py for the executable analytical model.
