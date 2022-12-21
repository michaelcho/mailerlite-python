<a href="https://www.mailerlite.com"><img src="https://app.mailerlite.com/assets/images/logo-color.png" width="200px"/></a>

# MailerLite Python SDK
[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)

## Getting started
For more information about MailerLite API, please visit the [following link:](https://developers.mailerlite.com/docs/#mailerlite-api)
### Authentication
API keys are a quick way to implement machine-to-machine authentication without any direct inputs from a human beyond initial setup.

For more information how to obtain an API key visit the [following link](https://developers.mailerlite.com/docs/#mailerlite-api)

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
  - [Subscribers](#subscribers)
    - [Get a list of subscribers](#get-a-list-of-subscribers)
    - [Get a single subscriber](#get-a-single-subscriber)
    - [Count all subscribers](#count-all-subscribers)
    - [Create a subscriber](#create-a-subscriber)
    - [Update a subscriber](#update-a-subscriber)
    - [Delete a subscriber](#delete-a-subscriber)
  - [Groups](#groups)
    - [Get a list of groups](#get-a-list-of-groups)
    - [Create a group](#create-a-group)
    - [Update a group](#update-a-group)
    - [Delete a group](#delete-a-group)
    - [Get subscribers belonging to a group](#get-subscribers-belonging-to-a-group)
    - [Assign subscriber to a group](#assign-subscribers-to-a-group)
  - [Segments](#segments)
    - [Get a list of segments](#get-a-list-of-segments)
    - [Update a segment](#update-a-segment)
    - [Delete a segment](#delete-a-segment)
    - [Get subscribers belonging to a segment](#get-subscribers-belonging-to-a-segment)
  - [Fields](#fields)
    - [Get a list of fields](#get-a-list-of-fields)
    - [Create a field](#create-a-field)
    - [Update a field](#update-a-field)
    - [Delete a field](#delete-a-field)
  - [Automations](#automations)
    - [Get a list of automations](#get-a-list-of-automations)
    - [Get an automation](#get-an-automation)
    - [Get subscribers activity for an automation](#get-subscribers-activity-for-an-automation)
  - [Campaigns](#campaigns)
    - [Get a list of campaigns](#get-a-list-of-campaigns)
    - [Get a campaign](#get-a-campaign)
    - [Create a campaign](#update-a-campaign)
    - [Update a campaign](#update-a-campaign)
    - [Schedule a campaign](#schedule-a-campaign)
    - [Cancel a ready campaign](#cancel-a-ready-campaign)
    - [Delete a campaign](#delete-a-campaign)
    - [Get subscribers activity for a campaign](#get-subscribers-activity-for-an-campaign)
  - [Forms](#forms)
    - [Get a list of forms](#get-a-list-of-forms)
    - [Get a form](#get-a-form)
    - [Update a form](#update-a-form)
    - [Delete a form](#delete-a-form)
    - [Get subscribers of a form](#get-subscribers-of-a-form)
  - [Batching](#batching)
    - [Create a new batch](#create-a-new-batch)
  - [Webhooks](#webhooks)
    - [Get a list of webhooks](#get-a-list-of-webhooks)
    - [Get a webhook](#get-a-webhook)
    - [Create a webhook](#update-a-webhook)
    - [Update a webhook](#update-a-webhook)
    - [Delete a webhook](#delete-a-webhook)
  - [Timezones](#timezones)
    - [Get a list of timezones](#get-a-list-of-timezones)
  - [Campaign languages](#languages)
    - [Get a list of languages](#get-a-list-of-languages)

<a name="installation"></a>
## Installation
Please run the following command:
```
$ python -m pip install mailerlite
```

<a name="usage"></a>
## Usage

The first thing that you need to do is to import `mailerlite` into your project and to instantiate the client by passing your API key:
```python
import mailerlite as MailerLite

client = MailerLite.Client({
  'api_key': 'your-api-key'
})
```

MailerLite API supports [versioning](https://developers.mailerlite.com/docs/#versioning), so you can pass additional argument to specify the API version:
```python
import mailerlite as MailerLite

client = MailerLite.Client({
  'api_key': 'your-api-key',
  'api_version': '2038-01-19'
})
```