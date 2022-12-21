<a href="https://www.mailerlite.com"><img src="https://app.mailerlite.com/assets/images/logo-color.png" width="200px"/></a>

# MailerLite Python SDK
[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)

## Getting started
For more information about MailerLite API, please visit the [following link:](https://developers.mailerlite.com/docs/#mailerlite-api)
### Authentication
API keys are a quick way to implement machine-to-machine authentication without any direct inputs from a human beyond initial setup.

For more information how to obtain an API key visit the [following link](https://developers.mailerlite.com/docs/#mailerlite-api)

## Table of Contents
- [MailerLite Python SDK](#mailerlite-python-sdk)
  - [Getting started](#getting-started)
    - [Authentication](#authentication)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
    - [MailerLite Client](#mailerlite-client)
  - [Subscribers](#subscribers)
    - [List all subscribers](#list-all-subscribers)
    - [Create a subscriber](#create-a-subscriber)
    - [Update a subscriber](#update-a-subscriber)
    - [Get a subscriber](#get-a-subscriber)
    - [Delete a subscriber](#delete-a-subscriber)
  - [Groups](#groups)
    - [List all groups](#list-all-groups)
    - [Create a group](#create-a-group)
    - [Update a group](#update-a-group)
    - [Delete a group](#delete-a-group)
    - [Get subscribers belonging to a group](#get-subscribers-belonging-to-a-group)
    - [Assign subscriber to a group](#assign-subscriber-to-a-group)
    - [Unassign subscriber from a group](#unassign-subscriber-from-a-group)

## Installation
<a name="installation"></a>

Please run the following command:
```bash
python -m pip install mailerlite
```

## Usage
<a name="usage"></a>

### MailerLite Client
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

## Subscribers
<a name="subscribers"></a>

### List all subscribers
<a name="get-a-list-of-subscribers"></a>

```python
import mailerlite as MailerLite

client = MailerLite.Client({
  'api_key': 'your-api-key'
})

response = client.subscribers.list(limit=10, page=1, filter={'status': 'active'})
```

### Create a subscriber
<a name="create-a-subscriber"></a>

```python
import mailerlite as MailerLite

client = MailerLite.Client({
  'api_key': 'your-api-key'
})

response = client.subscribers.create('some@email.com', fields={'name': 'John', 'last_name': 'Doe'}, ip_address='1.2.3.4', optin_ip='1.2.3.4')
```

### Update a subscriber
<a name="update-a-subscriber"></a>

```python
import mailerlite as MailerLite

client = MailerLite.Client({
  'api_key': 'your-api-key'
})

response = client.subscribers.update('some@email.com', fields={'name': 'New', 'last_name': 'Name'}, ip_address='1.2.3.5', optin_ip='1.2.3.5')
```

### Get a subscriber
<a name="get-a-subscriber"></a>

```python
import mailerlite as MailerLite

client = MailerLite.Client({
  'api_key': 'your-api-key'
})

response = client.subscribers.get('some@email.com')
```

### Delete a subscriber
<a name="delete-a-subscriber"></a>

```python
import mailerlite as MailerLite

client = MailerLite.Client({
  'api_key': 'your-api-key'
})

subscriber_id = 1234567890

response = client.subscribers.delete(subscriber_id)
```

## Groups
<a name="groups"></a>

### List all groups
<a name="list-all-groups"></a>

```python
import mailerlite as MailerLite

client = MailerLite.Client({
  'api_key': 'your-api-key'
})

response = client.groups.list(limit=10, page=1, filter={'name': 'My'}, sort='name')
```

### Create a group
<a name="create-a-group"></a>

```python
import mailerlite as MailerLite

client = MailerLite.Client({
  'api_key': 'your-api-key'
})

group_name = 'My Group'

response = client.groups.create(group_name)
```

### Update a group
<a name="update-a-group"></a>

```python
import mailerlite as MailerLite

client = MailerLite.Client({
  'api_key': 'your-api-key'
})

group_id = 1234567
group_name = 'My New Group'

response = client.groups.update(group_id, group_name)
```

### Delete a group
<a name="delete-a-group"></a>

```python
import mailerlite as MailerLite

client = MailerLite.Client({
  'api_key': 'your-api-key'
})

group_id = 1234567

response = client.groups.delete(group_id)
```

### Get subscribers belonging to a group
<a name="get-subscribers-belonging-to-a-group"></a>

```python
import mailerlite as MailerLite

client = MailerLite.Client({
  'api_key': 'your-api-key'
})

group_id = 1234567

response = client.groups.get_group_subscribers(group_id, page=1, limit=10, filter={'status': 'active'})
```

### Assign subscriber to a group
<a name="assign-subscribers-to-a-group"></a>

```python
import mailerlite as MailerLite

client = MailerLite.Client({
  'api_key': 'your-api-key'
})

subscriber_id = 111222
group_id = 1234567

response = client.subscribers.assign_subscriber_to_group(subscriber_id, group_id)
```

### Unassign subscriber from a group
<a name="unassign-subscribers-from-a-group"></a>

```python
import mailerlite as MailerLite

client = MailerLite.Client({
  'api_key': 'your-api-key'
})

subscriber_id = 111222
group_id = 1234567

response = client.subscribers.unassign_subscriber_from_group(subscriber_id, group_id)
```