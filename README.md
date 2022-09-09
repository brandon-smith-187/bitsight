# Unofficial Library for using the BitSight API

This library makes it easy to perform some of the most common BitSight tasks via the BitSight API, while accounting for
common responses and pagination.

## Official BitSight API Documentation:

- [BitSight Knowledge Base API Documentation](https://help.bitsighttech.com/hc/en-us/articles/231872628-API-Documentation-Overview)
- [v1 Swagger](https://service.bitsighttech.com/customer-api/v1/ui)
- [v2 Swagger](https://service.bitsighttech.com/customer-api/v2/ui)

## Setup:

```
pip install bitsight
```

#### Optional:

Set your BitSight API Token as an environment variable named BST_API_KEY. Otherwise, you will be prompted to enter your
api token.

## Example Usage:

```
import bitsight
```

### Search for a company

```
companies = bitsight.Companies()
search_results = companies.get_company_search('example.com')
```

### Subscribe to a company

```
guid = search_results[0]['guid']
subscriptions = bitsight.Subscriptions()
subscribe_result = subscriptions.post_subscribe(guid, bitsight.LicenseType.continuous_monitoring)
```

### Get findings for a company

```
findings = companies.get_findings(guid)
```

### Get risk vectors and rating history

```
company_details = companies.get_company_details(guid)
```

### Download a company report

```
reports = bitsight.Reports()
report_successful = reports.post_download_company_report(guid, file_path='example_report.pdf')
```

### Request a company

```
company_requests = bitsight.CompanyRequests()
company_request_response = company_requests.post_request_company('example.com')
```

### Request a fast ratings report for a company

```
rua = bitsight.RapidUnderwriting()
fast_ratings_report = rua.post_request_rua(domain='example.com', company_name='Example', industry=bitsight.Industries.technology)
```

### Get all companies in your portfolio

```
portfolio = bitsight.Portfolio()
portfolio_companies = portfolio.get_portfolio()
```

### Get the latest alerts for your portfolio

```
alerts = bitsight.Alerts()
latest_alerts = alerts.get_latest_alerts()
```

### Make any request

```
session_manager = bitsight.BitSight()
industries = session_manager.get(bitsight.Endpoints.V1.industries)
```


