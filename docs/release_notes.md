# Release Notes

## Release 1.3.3
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