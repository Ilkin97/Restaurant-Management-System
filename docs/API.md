# API Documentation

This document describes the available API endpoints for the project.

## Authentication

**Base URL:** `/api/auth/`

### Login
**Method:** `POST`

**Request:**
```json
{
    "email": "user@example.com",
    "password": "password"
}
