# checkout-service

Internal checkout and payments microservice. Handles cart processing,
payment method validation, and order confirmation for the platform.

## Structure

- `checkout_service.py` - core checkout flow
- `cache_config.py` - Redis cache configuration for checkout session data
- `payment_gateway.py` - payment provider integration
- `models.py` - data models for cart/order state

## Running locally

```
pip install -r requirements.txt
python -m pytest tests/
```

## On-call

This service is monitored by Chronicle for incident correlation. Recent
deploys are tracked automatically against incident reports.
