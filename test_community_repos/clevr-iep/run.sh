BASEDIR=$(dirname $0)
pushd $BASEDIR

git clone https://github.com/facebookresearch/clevr-iep.git
./download-data.sh
./install-deps.sh
./run-script.sh
RETURN=$?

# rm -rf clevr-iep
popd
exit $RETURN

