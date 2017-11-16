pushd fastai
conda install -y thinc
conda install -y spacy
pip install -r requirements.txt
pip install graphviz sklearn_pandas torchtext torchvision numba keras feather-format tensorflow
popd
