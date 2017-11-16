BASEDIR=$(dirname $0)
pushd $BASEDIR
git clone https://github.com/fastai/fastai
./download-data.sh
./install-deps.sh
./run-script.sh
RETURN=$?
# rm -rf fastai
popd
exit $RETURN

