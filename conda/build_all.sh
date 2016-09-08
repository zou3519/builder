#!/usr/bin/env bash
set -e

if [ -z "$ANACONDA_TOKEN" ]; then
    echo "ANACONDA_TOKEN is unset. Please set it in your environment before running this script";
    exit 1
fi

BUILD_VERSION="0.1.3"
BUILD_NUMBER=3

export PYTORCH_BUILD_VERSION=$BUILD_VERSION
export PYTORCH_BUILD_NUMBER=$BUILD_NUMBER

conda config --set anaconda_upload no

conda build --no-anaconda-upload --python 2.7 pytorch-$BUILD_VERSION
conda build --no-anaconda-upload --python 3.4 pytorch-$BUILD_VERSION
conda build --no-anaconda-upload --python 3.5 pytorch-$BUILD_VERSION

echo "All builds succeeded, uploading binaries"

set +e

anaconda -t $ANACONDA_TOKEN upload --user soumith $(conda build --python 2.7 pytorch-$BUILD_VERSION --output)
anaconda -t $ANACONDA_TOKEN upload --user soumith $(conda build --python 3.4 pytorch-$BUILD_VERSION --output)
anaconda -t $ANACONDA_TOKEN upload --user soumith $(conda build --python 3.5 pytorch-$BUILD_VERSION --output)

unset PYTORCH_BUILD_VERSION
unset PYTORCH_BUILD_NUMBER