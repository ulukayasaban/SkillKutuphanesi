# Scopes (overview)

Etsy uses OAuth scopes to gate access to sensitive resources.

Examples of scope patterns you will encounter:

- `shops_r`, `shops_w`
- `listings_r`, `listings_w`
- `transactions_r`
- `receipts_r`, `receipts_w`
- `profile_r`, `profile_w`
- `email_r`

The OpenAPI reference lists required authorizations per endpoint.

Agent guidance:
- Request the minimum set of scopes needed for the task.
- Scopes are fixed per refresh token; if you need new scopes you must re-run the authorization flow.
