#!/usr/bin/env bash

set -eo pipefail

echo "Configuring Java path..."
export PATH=/app/.apt/usr/lib/jvm/default-java/bin:$PATH
echo $PATH

echo "Installing Tika..."
wget -P scraper/tika-server/tika-server-1.23.jar https://www.apache.org/dyn/closer.cgi/tika/tika-server-1.23.jar
export TIKA_SERVER_JAR=$(pwd)/scraper/tika-server/tika-server-1.23.jar
echo $TIKA_SERVER_JAR

echo "Done!"
