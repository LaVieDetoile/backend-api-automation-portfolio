# Backend API Automation Portfolio

A safe public portfolio project that demonstrates backend/API test automation with Python, Pytest, Requests, Pydantic models, reusable API clients, shared fixtures, cleanup logic, linting, reporting, and GitHub Actions CI.

## Public Portfolio Disclaimer

This repository is a personal portfolio project. It does not contain company code, credentials, proprietary logic, internal URLs, tickets, client data, copied source code, or private test data. The framework uses only public demo APIs.

## APIs Under Test

- [Restful Booker](https://restful-booker.herokuapp.com/apidoc/index.html) for booking lifecycle, auth, filtering, update, delete, and health checks.
- [JSONPlaceholder](https://jsonplaceholder.typicode.com) for user/contact-style read-only API checks.

## Tech Stack

- Python
- Pytest
- Requests
- Pydantic typed models
- python-dotenv
- pytest-html
- Ruff
- GitHub Actions

## Folder Structure

```text
backend-api-automation-portfolio/
  backend_api_automation/
    clients/       # API client classes for auth, booking, health, users
    config/        # Settings loaded from environment variables
    fixtures/      # Shared Pytest fixtures and cleanup
    models/        # Typed request/response models
    utils/         # Assertions, builders, logging, retry helper
  tests/
    test_auth/
    test_bookings/
    test_health/
    test_users/
  test_data/       # Safe public demo payload builders
  .github/workflows/api-tests.yml
```

## Test Coverage

### Booking API

- Create booking
- Fetch created booking
- Update booking and verify updated values
- Partial update booking and verify unchanged fields are preserved
- Delete booking and verify it can no longer be fetched
- Validate booking IDs response shape
- Validate supported filtering by first name and date range

### Negative Coverage

- Invalid auth is rejected
- Update without valid auth is rejected
- Delete without valid auth is rejected
- Non-existing booking lookup is handled correctly
- Incomplete booking payload rejection is validated

### Health / Options-Style Coverage

- Validate `/ping` health endpoint
- Validate booking IDs endpoint as stable configuration/options-style data

### User / Contact-Style Coverage

- List users response
- Single user response
- User not-found behavior
- Nested user posts resource

## Install

```bash
poetry install
```

Optional local environment file:

```bash
cp .env.example .env
```

Never commit `.env`.

## Run Tests

```bash
poetry run pytest
poetry run pytest -m smoke
poetry run pytest -m regression
poetry run pytest -m negative
```

HTML report output:

```text
reports/api-test-report.html
```

## Run Lint

```bash
poetry run ruff check .
poetry run ruff format .
```

## GitHub Actions

The CI workflow runs on `push` and `pull_request`. It checks out the repository, installs Python and Poetry, installs dependencies, runs Ruff linting, runs the Pytest API suite, and uploads the HTML report as an artifact.

## What Interviewers Should Notice

- Tests use API clients instead of raw request calls spread across test files.
- Pydantic models validate response contracts and make failures easier to diagnose.
- Fixtures centralize client setup, auth token creation, and booking cleanup.
- Data builders keep test payloads readable and reusable.
- Assertions include clear failure messages.
- Tests are grouped by API domain and remain independent.
- No arbitrary sleeps are used.
- Public APIs and public demo credentials keep the project safe to share.

## Public Safety Statement

No company code, credentials, internal URLs, client IDs, tickets, proprietary business logic, internal test data, reports, screenshots, videos, or private repository code are included.

## Create and Push Public GitHub Repo

After authenticating GitHub CLI with the intended account, run:

```bash
cd /Users/laurautarbayeva/Desktop/repos/backend-api-automation-portfolio
gh auth status
gh repo create LauraUtar/backend-api-automation-portfolio --public --source=. --remote=origin --push
```
