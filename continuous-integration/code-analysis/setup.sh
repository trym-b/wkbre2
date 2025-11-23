#!/bin/bash

set -euo pipefail

SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
REPO_ROOT_DIR=$(cd "${SCRIPT_DIR}/../.." && pwd)

"$REPO_ROOT_DIR/continuous-integration/common/install_uv.sh"

uv sync
