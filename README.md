# Opensea Checker

This repository contains scripts that utilize the OpenSea API to automate tasks related to NFT data analysis. Current functionalities include fetching the minimum price (floor price) of specified NFT collections and analyzing the latest listing events on OpenSea.

- [OpenSea's Developer Platform](https://docs.opensea.io/)
- [OpenSea Status](https://status.opensea.io/)
- [OpenSea's Dune Dashboard](https://dune.com/rchen8/opensea)

## Python Workflow

Set local python environment

```bash
python3 -m venv venv
```

Start environment

```bash
source venv/bin/activate
```

Stop environment

```bash
deactivate
```

## .ENV file exmpl

```text
API_KEY_OPENSEA=your-api-key-here
API_PATH_OPENSEA=https://api.opensea.io/api/v2

```

## Data. slugs.json exmpl

```json
["azuki", "clonex", ]
```
