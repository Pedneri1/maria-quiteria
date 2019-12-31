#!/usr/bin/env bash

set -eo pipefail

echo "Installing Tika..."
wget -P scraper/tika-server/tika-server-1.23.jar https://www.apache.org/dyn/closer.cgi/tika/tika-server-1.23.jar
export TIKA_SERVER_JAR=$(pwd)/scraper/tika-server/tika-server-1.23.jar
echo TIKA_SERVER_JAR=$TIKA_SERVER_JAR

echo "Done!"
