[![Build Status](https://travis-ci.org/EvidentSecurity/esp-sdk-python2.svg?branch=master)](https://travis-ci.org/EvidentSecurity/esp-sdk-python2)
[![Gem Version](https://badge.fury.io/py/esp-sdk-python2.svg)](http://badge.fury.io/py/esp-sdk-python2)

# esp_sdk
No descripton provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v2
- Package version: 1.0.0
- Build date: 2017-04-12T14:50:05.641-04:00
- Build package: class io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import esp_sdk 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import esp_sdk
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = esp_sdk.AlertsApi()
report_id = 56 # int | Id of the Report to Return Alerts For
page = {'key': 'page_example'} # dict(str, str) | Page Number (optional)
filter = {'key': 'filter_example'} # dict(str, str) | Filter Params for Searching (optional)
include = 'include_example' # str | Included Objects (optional)
region_id = 56 # int | Return only alerts for this region. (optional)
status = 'status_example' # str | Return only alerts for the give status(es). Valid values are fail, warn, error, pass, info (optional)
first_seen = 56 # int | Return only alerts that have started within a number of hours of the report. For example, first_seen of 3 will return alerts that started showing up within the last 3 hours of the report. (optional)
suppressed = true # bool | Return only suppressed alerts (optional)
team_id = 56 # int | Return only alerts for the given team. (optional)
external_account_id = 56 # int | Return only alerts for the given external id. (optional)
service_id = 56 # int | Return only alerts on signatures with the given service. (optional)
signature_severity = 'signature_severity_example' # str | Return only alerts for signatures with the given risk_level. Valid values are Low, Medium, High (optional)
signature_name = 'signature_name_example' # str | Return only alerts for signatures with the given name. (optional)
resource = 'resource_example' # str | Return only alerts for the given resource or tag. (optional)
signature_identifier = 'signature_identifier_example' # str | Return only alerts for signatures with the given identifier. (optional)

try:
    # Get a list of Alerts
    api_response = api_instance.list(report_id, page=page, filter=filter, include=include, region_id=region_id, status=status, first_seen=first_seen, suppressed=suppressed, team_id=team_id, external_account_id=external_account_id, service_id=service_id, signature_severity=signature_severity, signature_name=signature_name, resource=resource, signature_identifier=signature_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->list: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost/*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AlertsApi* | [**list**](docs/AlertsApi.md#list) | **PUT** /api/v2/reports/{report_id}/alerts.json_api | Get a list of Alerts
*AlertsApi* | [**show**](docs/AlertsApi.md#show) | **GET** /api/v2/alerts/{id}.json_api | Show a single Alert
*CloudTrailEventsApi* | [**list**](docs/CloudTrailEventsApi.md#list) | **GET** /api/v2/alerts/{alert_id}/cloud_trail_events.json_api | Get a list of Cloud Trail Events
*CloudTrailEventsApi* | [**show**](docs/CloudTrailEventsApi.md#show) | **GET** /api/v2/cloud_trail_events/{id}.json_api | Show a single Cloud Trail Event
*ContactRequestsApi* | [**create**](docs/ContactRequestsApi.md#create) | **POST** /api/v2/contact_requests.json_api | Create a(n) Contact Request
*CustomSignatureDefinitionsApi* | [**create**](docs/CustomSignatureDefinitionsApi.md#create) | **POST** /api/v2/custom_signature_definitions.json_api | Create a(n) Definition
*CustomSignatureDefinitionsApi* | [**destroy**](docs/CustomSignatureDefinitionsApi.md#destroy) | **DELETE** /api/v2/custom_signature_definitions/{id}.json_api | Remove a(n) Definition
*CustomSignatureDefinitionsApi* | [**list**](docs/CustomSignatureDefinitionsApi.md#list) | **PUT** /api/v2/custom_signature_definitions.json_api | Get a list of Definitions
*CustomSignatureDefinitionsApi* | [**show**](docs/CustomSignatureDefinitionsApi.md#show) | **GET** /api/v2/custom_signature_definitions/{id}.json_api | Show a single Definition
*CustomSignatureDefinitionsApi* | [**update**](docs/CustomSignatureDefinitionsApi.md#update) | **PATCH** /api/v2/custom_signature_definitions/{id}.json_api | Update a(n) Definition
*CustomSignatureResultsApi* | [**create**](docs/CustomSignatureResultsApi.md#create) | **POST** /api/v2/custom_signature_results.json_api | Create a(n) Result
*CustomSignatureResultsApi* | [**list**](docs/CustomSignatureResultsApi.md#list) | **PUT** /api/v2/custom_signature_results.json_api | Get a list of Results
*CustomSignatureResultsApi* | [**show**](docs/CustomSignatureResultsApi.md#show) | **GET** /api/v2/custom_signature_results/{id}.json_api | Show a single Result
*CustomSignatureStatsApi* | [**list**](docs/CustomSignatureStatsApi.md#list) | **GET** /api/v2/stats/{stat_id}/custom_signatures.json_api | A successful call to this API returns all the stats of all the custom signatures for a report identified by the stat_id parameter. Said report contains all statistics for this alert triggered from signatures contained in all custom_signatures for the selected hour.
*CustomSignaturesApi* | [**create**](docs/CustomSignaturesApi.md#create) | **POST** /api/v2/custom_signatures.json_api | Create a(n) Custom Signature
*CustomSignaturesApi* | [**destroy**](docs/CustomSignaturesApi.md#destroy) | **DELETE** /api/v2/custom_signatures/{id}.json_api | Remove a(n) Custom Signature
*CustomSignaturesApi* | [**list**](docs/CustomSignaturesApi.md#list) | **PUT** /api/v2/custom_signatures.json_api | Get a list of Custom Signatures
*CustomSignaturesApi* | [**show**](docs/CustomSignaturesApi.md#show) | **GET** /api/v2/custom_signatures/{id}.json_api | Show a single Custom Signature
*CustomSignaturesApi* | [**update**](docs/CustomSignaturesApi.md#update) | **PATCH** /api/v2/custom_signatures/{id}.json_api | Update a(n) Custom Signature
*DashboardApi* | [**recent**](docs/DashboardApi.md#recent) | **GET** /api/v2/dashboard/recent.json_api | 
*ExternalAccountsApi* | [**api_v2_external_accounts_id_complete_json_api_patch**](docs/ExternalAccountsApi.md#api_v2_external_accounts_id_complete_json_api_patch) | **PATCH** /api/v2/external_accounts/{id}/complete.json_api | Show the latest completed report for an External Account
*ExternalAccountsApi* | [**api_v2_external_accounts_subscribed_accounts_json_api_get**](docs/ExternalAccountsApi.md#api_v2_external_accounts_subscribed_accounts_json_api_get) | **GET** /api/v2/external_accounts/subscribed_accounts.json_api | Show a list of Subscribed Accounts
*ExternalAccountsApi* | [**create**](docs/ExternalAccountsApi.md#create) | **POST** /api/v2/external_accounts.json_api | Create a(n) External Account
*ExternalAccountsApi* | [**destroy**](docs/ExternalAccountsApi.md#destroy) | **DELETE** /api/v2/external_accounts/{id}.json_api | Remove a(n) External Account
*ExternalAccountsApi* | [**list**](docs/ExternalAccountsApi.md#list) | **PUT** /api/v2/external_accounts.json_api | Get a list of External Accounts
*ExternalAccountsApi* | [**show**](docs/ExternalAccountsApi.md#show) | **GET** /api/v2/external_accounts/{id}.json_api | Show a single External Account
*ExternalAccountsApi* | [**update**](docs/ExternalAccountsApi.md#update) | **PATCH** /api/v2/external_accounts/{id}.json_api | Update a(n) External Account
*MetadataApi* | [**for_alert**](docs/MetadataApi.md#for_alert) | **GET** /api/v2/alerts/{alert_id}/metadata.json_api | Show the metadata for an alert
*MetadataApi* | [**show**](docs/MetadataApi.md#show) | **GET** /api/v2/metadata/{id}.json_api | Show a single Metadata
*OrganizationsApi* | [**list**](docs/OrganizationsApi.md#list) | **PUT** /api/v2/organizations.json_api | Get a list of Organizations
*OrganizationsApi* | [**show**](docs/OrganizationsApi.md#show) | **GET** /api/v2/organizations/{id}.json_api | Show a single Organization
*OrganizationsApi* | [**update**](docs/OrganizationsApi.md#update) | **PATCH** /api/v2/organizations/{id}.json_api | Update a(n) Organization
*RegionStatsApi* | [**list**](docs/RegionStatsApi.md#list) | **GET** /api/v2/stats/{stat_id}/regions.json_api | A successful call to this API returns all the stats of all the regions for a report identified by the stat_id parameter. Said report contains all statistics for this alert triggered from signatures contained in all regions for the selected hour.
*RegionSuppressionsApi* | [**create_region_suppression**](docs/RegionSuppressionsApi.md#create_region_suppression) | **POST** /api/v2/suppressions/regions.json_api | A successful call to this API creates a new region suppression for the supplied regions . The body of the request must contain a json api compliant hash of attributes with type suppression/regions.
*RegionsApi* | [**list**](docs/RegionsApi.md#list) | **PUT** /api/v2/regions.json_api | Get a list of Regions
*RegionsApi* | [**show**](docs/RegionsApi.md#show) | **GET** /api/v2/regions/{id}.json_api | Show a single Region
*ReportsApi* | [**create**](docs/ReportsApi.md#create) | **POST** /api/v2/reports.json_api | Create a(n) Report
*ReportsApi* | [**list**](docs/ReportsApi.md#list) | **PUT** /api/v2/reports.json_api | Get a list of Reports
*ReportsApi* | [**show**](docs/ReportsApi.md#show) | **GET** /api/v2/reports/{id}.json_api | Show a single Report
*RolesApi* | [**list**](docs/RolesApi.md#list) | **GET** /api/v2/roles.json_api | Get a list of Roles
*RolesApi* | [**show**](docs/RolesApi.md#show) | **GET** /api/v2/roles/{id}.json_api | Show a single Role
*ScanIntervalsApi* | [**create**](docs/ScanIntervalsApi.md#create) | **POST** /api/v2/scan_intervals.json_api | Create a(n) Scan Interval
*ScanIntervalsApi* | [**destroy**](docs/ScanIntervalsApi.md#destroy) | **DELETE** /api/v2/scan_intervals/{id}.json_api | Remove a(n) Scan Interval
*ScanIntervalsApi* | [**list**](docs/ScanIntervalsApi.md#list) | **GET** /api/v2/external_accounts/{external_account_id}/scan_intervals.json_api | Get a list of Scan Intervals
*ScanIntervalsApi* | [**show**](docs/ScanIntervalsApi.md#show) | **GET** /api/v2/scan_intervals/{id}.json_api | Show a single Scan Interval
*ScanIntervalsApi* | [**update**](docs/ScanIntervalsApi.md#update) | **PATCH** /api/v2/scan_intervals/{id}.json_api | Update a(n) Scan Interval
*ServiceStatsApi* | [**list**](docs/ServiceStatsApi.md#list) | **GET** /api/v2/stats/{stat_id}/services.json_api | A successful call to this API returns all the stats of all the services for a report identified by the stat_id parameter. Said report contains all statistics for this alert triggered from signatures contained in all regions for the selected hour.
*ServicesApi* | [**list**](docs/ServicesApi.md#list) | **GET** /api/v2/services.json_api | Get a list of Services
*ServicesApi* | [**show**](docs/ServicesApi.md#show) | **GET** /api/v2/services/{id}.json_api | Show a single Service
*SignatureCustomRiskLevelsApi* | [**create**](docs/SignatureCustomRiskLevelsApi.md#create) | **POST** /api/v2/signature_custom_risk_levels.json_api | Create a(n) Signature Custom Risk Level
*SignatureCustomRiskLevelsApi* | [**destroy**](docs/SignatureCustomRiskLevelsApi.md#destroy) | **DELETE** /api/v2/signature_custom_risk_levels/{id}.json_api | Remove a(n) Signature Custom Risk Level
*SignatureCustomRiskLevelsApi* | [**list**](docs/SignatureCustomRiskLevelsApi.md#list) | **GET** /api/v2/external_accounts/{external_account_id}/signature_custom_risk_levels.json_api | Get a list of Signature Custom Risk Levels
*SignatureCustomRiskLevelsApi* | [**show**](docs/SignatureCustomRiskLevelsApi.md#show) | **GET** /api/v2/signature_custom_risk_levels/{id}.json_api | Show a single Signature Custom Risk Level
*SignatureCustomRiskLevelsApi* | [**update**](docs/SignatureCustomRiskLevelsApi.md#update) | **PATCH** /api/v2/signature_custom_risk_levels/{id}.json_api | Update a(n) Signature Custom Risk Level
*SignatureStatsApi* | [**list**](docs/SignatureStatsApi.md#list) | **GET** /api/v2/stats/{stat_id}/signatures.json_api | A successful call to this API returns all the stats of all the signatures for a report identified by the stat_id parameter. Said report contains all statistics for this alert triggered from signatures contained in all signatures for the selected hour.
*SignatureSuppressionsApi* | [**create_signature_suppression**](docs/SignatureSuppressionsApi.md#create_signature_suppression) | **POST** /api/v2/suppressions/signatures.json_api | A successful call to this API creates a new signature suppression for the supplied signature_ids or custom_signature_ids. The body of the request must contain a json API compliant hash of attributes with type suppression/signatures.
*SignaturesApi* | [**list**](docs/SignaturesApi.md#list) | **PUT** /api/v2/signatures.json_api | Get a list of Signatures
*SignaturesApi* | [**run**](docs/SignaturesApi.md#run) | **POST** /api/v2/signatures/{id}/run.json_api | Run a Signature
*SignaturesApi* | [**show**](docs/SignaturesApi.md#show) | **GET** /api/v2/signatures/{id}.json_api | Show a single Signature
*StatsApi* | [**for_report**](docs/StatsApi.md#for_report) | **GET** /api/v2/reports/{report_id}/stats.json_api | A successful call to this API returns all the stats of all the alerts for a report identified by the report_id parameter. Said report contains all statistics for this alert triggered from signatures contained in all regions for the selected hour.
*StatsApi* | [**latest_for_teams**](docs/StatsApi.md#latest_for_teams) | **GET** /api/v2/stats/latest_for_teams.json_api | A successful call to this API returns all the stats for the most recent report of each team accessible by the given API key
*SubOrganizationsApi* | [**create**](docs/SubOrganizationsApi.md#create) | **POST** /api/v2/sub_organizations.json_api | Create a(n) Sub Organization
*SubOrganizationsApi* | [**destroy**](docs/SubOrganizationsApi.md#destroy) | **DELETE** /api/v2/sub_organizations/{id}.json_api | Remove a(n) Sub Organization
*SubOrganizationsApi* | [**list**](docs/SubOrganizationsApi.md#list) | **PUT** /api/v2/sub_organizations.json_api | Get a list of Sub Organizations
*SubOrganizationsApi* | [**show**](docs/SubOrganizationsApi.md#show) | **GET** /api/v2/sub_organizations/{id}.json_api | Show a single Sub Organization
*SubOrganizationsApi* | [**update**](docs/SubOrganizationsApi.md#update) | **PATCH** /api/v2/sub_organizations/{id}.json_api | Update a(n) Sub Organization
*SuppressionsApi* | [**deactivate**](docs/SuppressionsApi.md#deactivate) | **PATCH** /api/v2/suppressions/{id}/deactivate.json_api | A successful call to this API will deactivate a suppression identified by the id parameter.
*SuppressionsApi* | [**list**](docs/SuppressionsApi.md#list) | **PUT** /api/v2/suppressions.json_api | Get a list of Suppressions
*SuppressionsApi* | [**show**](docs/SuppressionsApi.md#show) | **GET** /api/v2/suppressions/{id}.json_api | Show a single Suppression
*TagsApi* | [**list**](docs/TagsApi.md#list) | **GET** /api/v2/alerts/{alert_id}/tags.json_api | Get a list of Tags
*TagsApi* | [**show**](docs/TagsApi.md#show) | **GET** /api/v2/tags/{id}.json_api | Show a single Tag
*TeamsApi* | [**create**](docs/TeamsApi.md#create) | **POST** /api/v2/teams.json_api | Create a(n) Team
*TeamsApi* | [**destroy**](docs/TeamsApi.md#destroy) | **DELETE** /api/v2/teams/{id}.json_api | Remove a(n) Team
*TeamsApi* | [**list**](docs/TeamsApi.md#list) | **PUT** /api/v2/teams.json_api | Get a list of Teams
*TeamsApi* | [**show**](docs/TeamsApi.md#show) | **GET** /api/v2/teams/{id}.json_api | Show a single Team
*TeamsApi* | [**update**](docs/TeamsApi.md#update) | **PATCH** /api/v2/teams/{id}.json_api | Update a(n) Team
*TimeZonesApi* | [**list**](docs/TimeZonesApi.md#list) | **GET** /api/v2/time_zones.json_api | A successful call to this API returns a list of time zones.
*UsersApi* | [**create**](docs/UsersApi.md#create) | **POST** /api/v2/users.json_api | Create a(n) User
*UsersApi* | [**destroy**](docs/UsersApi.md#destroy) | **DELETE** /api/v2/users/{id}.json_api | Remove a(n) User
*UsersApi* | [**list**](docs/UsersApi.md#list) | **PUT** /api/v2/users.json_api | Get a list of Users
*UsersApi* | [**show**](docs/UsersApi.md#show) | **GET** /api/v2/users/{id}.json_api | Show a single User
*UsersApi* | [**update**](docs/UsersApi.md#update) | **PATCH** /api/v2/users/{id}.json_api | Update a(n) User


## Documentation For Models

 - [Alert](docs/Alert.md)
 - [CloudTrailEvent](docs/CloudTrailEvent.md)
 - [ContactRequest](docs/ContactRequest.md)
 - [CustomSignature](docs/CustomSignature.md)
 - [CustomSignatureDefinition](docs/CustomSignatureDefinition.md)
 - [Definition](docs/Definition.md)
 - [ExternalAccount](docs/ExternalAccount.md)
 - [Metadata](docs/Metadata.md)
 - [Organization](docs/Organization.md)
 - [PaginatedCollection](docs/PaginatedCollection.md)
 - [Region](docs/Region.md)
 - [Report](docs/Report.md)
 - [Result](docs/Result.md)
 - [Role](docs/Role.md)
 - [ScanInterval](docs/ScanInterval.md)
 - [Service](docs/Service.md)
 - [Signature](docs/Signature.md)
 - [SignatureCustomRiskLevel](docs/SignatureCustomRiskLevel.md)
 - [Stat](docs/Stat.md)
 - [StatCustomSignature](docs/StatCustomSignature.md)
 - [StatRegion](docs/StatRegion.md)
 - [StatService](docs/StatService.md)
 - [StatSignature](docs/StatSignature.md)
 - [SubOrganization](docs/SubOrganization.md)
 - [Suppression](docs/Suppression.md)
 - [Tag](docs/Tag.md)
 - [Team](docs/Team.md)
 - [TimeZone](docs/TimeZone.md)
 - [User](docs/User.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author



