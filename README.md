# OpenSea Checker

This repository contains scripts that utilize the OpenSea API to automate tasks related to NFT data analysis. Current functionalities include fetching the minimum price (floor price) of specified NFT collections on OpenSea.

- [OpenSea NFT Markeplace](https://opensea.io/)
- [OpenSea's Developer Platform](https://docs.opensea.io/)
- [OpenSea Status](https://status.opensea.io/)
- [OpenSea's Dune Dashboard](https://dune.com/rchen8/opensea)

## Datasets

### .env file exmpl

```text
API_KEY_OPENSEA=your-api-key-here
API_PATH_OPENSEA=https://api.opensea.io/api/v2
DATA_FOLDER=data/
```

### slugs.json exmpl

```json
["azuki", "boredapeyachtclub", "clonex"]
```

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
