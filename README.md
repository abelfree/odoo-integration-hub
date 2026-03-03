# Odoo Integration Hub

[![Odoo](https://img.shields.io/badge/Odoo-16%2B-5E2750)](https://www.odoo.com/)
[![License: LGPL-3.0](https://img.shields.io/badge/License-LGPL--3.0-blue.svg)](./LICENSE)
[![Status](https://img.shields.io/badge/Status-Portfolio_Ready-brightgreen)](#)
[![Last Commit](https://img.shields.io/github/last-commit/abelfree/odoo-integration-hub)](https://github.com/abelfree/odoo-integration-hub/commits/master)


## Problem
Odoo ecosystems often depend on external payments, messaging, and analytics services. Network errors and dependency outages can cause silent data loss without strong retry and failure tracking patterns.

## Solution
This project provides a connector job model with retry/backoff mechanics and a mock integration server for demonstrations.

## What It Demonstrates
- Connector job state management (`pending`, `done`, `failed`)
- Exponential backoff retry strategy
- Operational runbook for support teams
- Local mock HTTP endpoints for demos

## Architecture
- `addons/integration_hub/models/connector_job.py`
- `scripts/mock_endpoints.py`
- `docs/operational_runbook.md`

## Demo Flow
1. Start mock server: `python scripts/mock_endpoints.py`.
2. Create connector jobs in Odoo.
3. Execute retry-capable sender workflow.
4. Review retries and terminal states for observability.

## Portfolio Talking Points
- How retry policy protects business operations during transient outages.
- Why explicit failed-state handling reduces MTTR.
- How to separate connector domain logic from transport implementation.



