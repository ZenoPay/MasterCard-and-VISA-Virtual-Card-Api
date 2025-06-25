# MasterCard-and-VISA-Virtual-Card-Api


Manage virtual cardholders who own virtual cards via these API endpoints.

## Base URL

```

[https://zenoapi.com/api/payments/](https://zenoapi.com/api/payments/)

```

## Authentication

Include your API key in the request headers:

```

x-api-key: YOUR\_API\_KEY

````

---

## Endpoints

| Action                | Method | Endpoint                             | Description                             |
|-----------------------|--------|--------------------------------------|-----------------------------------------|
| Create a Cardholder   | POST   | `/cardholders/`                      | Register a new cardholder               |
| List All Cardholders  | GET    | `/my_cardholders/`                  | Retrieve all cardholders                |
| Get Cardholder by ID  | GET    | `/my_cardholders_byId/{id}/`        | Get a specific cardholder's details     |

---

## 1. Create a Cardholder

Register a new cardholder (who will own virtual cards).

### Request

```http
POST /cardholders/
Host: zenoapi.com
x-api-key: YOUR_API_KEY
Content-Type: application/json
````

### Request Body Fields

| Field        | Type   | Required | Description                          | Example                                         |
| ------------ | ------ | -------- | ------------------------------------ | ----------------------------------------------- |
| firstName    | string | Yes      | Cardholder’s first name              | "Juma"                                     |
| lastName     | string | Yes      | Cardholder’s last name               | "Komba"                                       |
| email        | string | Yes      | Email address                        | "[customer@mail.com](mailto:customer@mail.com)" |
| phone        | string | Yes      | Phone with country code              | "+255652534449389"                              |
| dateOfBirth  | string | Yes      | Format: YYYY-MM-DD                   | "1990-02-28"                                    |
| gender       | string | Yes      | `MALE` or `FEMALE`                   | "MALE"                                          |
| address      | string | Yes      | Street address                       | "Sinza Mori"                                    |
| city         | string | Yes      | City                                 | "Dar es Salaam"                                 |
| state        | string | Yes      | State or region                      | "Dar es Salaam"                                 |
| zipCode      | string | No       | ZIP or postal code                   | "12345"                                         |
| country      | string | Yes      | ISO Alpha-2 code                     | "TZ"                                            |
| documentType | string | Yes      | ID document type (e.g. NATIONAL\_ID) | "NATIONAL\_ID"                                  |

### Example (cURL)

```bash
curl -X POST "https://zenoapi.com/api/payments/cardholders/" \
  -H "x-api-key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "firstName": "Juma",
    "lastName": "Komba",
    "email": "customer@mail.com",
    "phone": "+255652534449389",
    "dateOfBirth": "1990-02-28",
    "gender": "MALE",
    "address": "Sinza Mori",
    "city": "Dar es salaam",
    "state": "Dar es salaam",
    "zipCode": "12345",
    "country": "TZ",
    "documentType": "NATIONAL_ID"
  }'
```

### Success Response

```json
{
  "status": "SUCCESS",
  "resultCode": "000",
  "message": "Cardholder created successfully",
  "cardholderId": "2af4183aa04c566005370e29ef158b1c81ae"
}
```

---

## 2. List All Cardholders

### Request

```http
GET /my_cardholders/
Host: zenoapi.com
x-api-key: YOUR_API_KEY
```

### Example (cURL)

```bash
curl -X GET "https://zenoapi.com/api/payments/my_cardholders/" \
  -H "x-api-key: YOUR_API_KEY"
```

### Success Response

```json
{
  "status": "SUCCESS",
  "resultCode": "000",
  "message": "Cardholder(s) fetched successfully",
  "cardholders": [
    {
      "first_name": "Juma",
      "last_name": "Komba",
      "email": "customer@mail.com",
      "phone": "+255652534449389",
      "address": "Sinza Mori",
      "city": "Dar es salaam",
      "state": "Dar es salaam",
      "zip_code": "12345",
      "country": "TZ",
      "document_type": "NATIONAL_ID",
      "document_number": "A13sdgsdofsfsi467",
      "id_front_url": "https://example.com/id_front.jpg",
      "id_back_url": null,
      "id_selfie_url": "https://example.com/id_selfie.jpg",
      "card_holder_id": "2af4183aa04c566005370e29ef158b1c81ae",
      "created_at": "2025-06-19T05:52:29.533741Z"
    }
  ]
}
```

---

## 3. Get Cardholder by ID

### Request

```http
GET /my_cardholders_byId/{card_holder_id}/
Host: zenoapi.com
x-api-key: YOUR_API_KEY
```

### Example (cURL)

```bash
curl -X GET "https://zenoapi.com/api/payments/my_cardholders_byId/2af4183aa04c566005370e29ef158b1c81ae/" \
  -H "x-api-key: YOUR_API_KEY"
```

### Success Response

```json
{
  "status": "SUCCESS",
  "resultCode": "000",
  "message": "Cardholder details fetched successfully",
  "cardholder": {
    "cardholder_id": "2af4183aa04c566005370e29ef158b1c81ae",
    "first_name": "Jumlpanji",
    "last_name": "Komplba",
    "email": "customer@mail.com",
    "phone": "+255652534449389",
    "address": "Sinza Mori",
    "city": "Dar es Salaam",
    "state": "Dar es Salaam",
    "zip_code": "12345",
    "country": "TZ",
    "document_type": "NATIONAL_ID",
    "document_number": "A13sdgsdofsfsi467",
    "id_front_url": "https://example.com/id_front.jpg",
    "id_back_url": null,
    "id_selfie_url": "https://example.com/id_selfie.jpg",
    "created_at": "2025-06-19T05:52:29.533741Z"
  }
}
```

---

## API Response Status Codes

| HTTP Status      | Code             | Description                 |
| ---------------- | ---------------- | --------------------------- |
| 200 OK           | `000`            | Operation successful        |
| 201 Created      | `000`            | New resource created        |
| 400 Bad Request  | `ERR_VALIDATION` | Validation error            |
| 401 Unauthorized | `ERR_AUTH_401`   | Invalid/missing API key     |
| 403 Forbidden    | `ERR_FORBIDDEN`  | No permission               |
| 404 Not Found    | `ERR_NOT_FOUND`  | Resource not found          |
| 409 Conflict     | `ERR_CONFLICT`   | Conflict with existing data |
| 500 Server Error | `ERR_SERVER_500` | Internal server error       |

### Error Response Format

```json
{
  "status": "ERROR",
  "resultCode": "ERR_CODE",
  "message": "Error description"
}
```

---

## Need Help?

📧 Email: [support@zenoapi.com](mailto:support@zenoapi.com)
📚 Docs: [https://zenoapi.com/docs](https://zenoapi.com/docs)

---

> © 2025 Zeno Limited. All rights reserved.

