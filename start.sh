#!/bin/sh

export NEW_RELIC_APP_NAME="Simple Django (LiC)"
export NEW_RELIC_LICENSE_KEY=
export NEW_RELIC_HIGH_SECURITY=false
export NEW_RELIC_DISTRIBUTED_TRACING_ENABLED=true
export NEW_RELIC_LOG_LEVEL=error

SCRIPTPATH="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

newrelic-admin run-python $SCRIPTPATH/app/manage.py runserver