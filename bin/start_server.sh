#!/bin/bash

set -euo pipefail

ENVIRONMENT="${ENVIRONMENT:-development}"
HOST='0.0.0.0'

if [[ ! "$ENVIRONMENT" =~ ^(development|production)$ ]]; then
    echo "Invalid \$ENVIRONMENT. Must be either \`development\` or \`production\`."
    exit 1
fi

if [[ "$ENVIRONMENT" == 'development' ]]; then
    fastapi dev \
        --host "$HOST" \
        src/main.py
fi
