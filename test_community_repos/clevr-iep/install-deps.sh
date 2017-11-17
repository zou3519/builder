pushd clevr-iep

# Get rid of pinned pytroch 0.1.11 dep
sed -i -e 's>http://download.pytorch.org/whl/cu80/torch-0.1.11.post5-cp35-cp35m-linux_x86_64.whl>>g' requirements.txt
pip install -r requirements.txt

popd

