#!/usr/bin/env sh

set -x
yarn run build
set +x


set -x
yarn start &
sleep 1
yarn test
echo $! > .pidfile
set +x
