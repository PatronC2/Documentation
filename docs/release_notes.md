# Release Notes

## Release v1.3.5
* Bump all golang Patron apps to go 1.24.3
* Bump UI to node 24
* Linux Agents no longer officially supported for kernels older than 3.2

## Release v1.3.4
* Use multi-stage build for the UI
* Reduce the size of the UI image
* Reduce frontend startup time
* Fix bug in Payloads page, where the "Delete" button was not visible when working in airgapped environments.

## Release v1.3.3
* Added the `/api/agents/search` API endpoint to return specific agents based on attributes
* Added the `/api/agentsmetrics` API endpoint to return Online / Offline agents
* Added the `/api/tags/options` API endpoint to return all tag key/value combinations
* Updated the UI to use the above endpoints in the Home page.
* Cleaned up minor UI bugs

## Release v1.3.2
* Docker Compose for redirectors
* Redirectors use API to update key and certificate for listeners

## Release v1.3.1
* Refactor agent code to move configuration requests into the client_utils
* Fix bug where agents show as offline while changing the callback frequency

## Release v1.3.0
* This is the first stable release of Patron