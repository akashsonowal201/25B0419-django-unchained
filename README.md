# Django Unchained - Wild West Bounty Board API

## Overview

This project is a REST API built using Django REST Framework for the Django Unchained assignment.

**Frontier Chosen:** 🎯 Bounty Board

Users can register, log in using JWT authentication, and manage their own bounty records. Each user can only access their own bounties.

## Features

- User Registration
- JWT Authentication (Access & Refresh Tokens)
- Create, Read, Update and Delete Bounties
- Ownership-based Access Control
- Rate Limiting (Bonus)
- Caching with Cache Invalidation (Bonus)

## API Endpoints

| Method | Endpoint |
|--------|----------|
| POST | `/api/auth/register/` |
| POST | `/api/auth/login/` |
| POST | `/api/auth/refresh/` |
| GET, POST | `/api/bounties/` |
| GET, PUT, PATCH, DELETE | `/api/bounties/<id>/` |

## Bonus Features

- **Rate Limiting:** Limits the number of API requests per user.
- **Caching:** The bounty list is cached, and the cache is automatically cleared whenever a bounty is created, updated, or deleted.

## Installation

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
