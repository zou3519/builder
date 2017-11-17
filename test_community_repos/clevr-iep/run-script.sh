pushd clevr-iep

# scripts need to be in top directory for iep import

mv scripts/* .
python run_model.py \
  --program_generator models/CLEVR/program_generator_18k.pt \
  --execution_engine models/CLEVR/execution_engine_18k.pt \
  --image img/CLEVR_val_000013.png \
  --question "Does the small sphere have the same color as the cube left of the gray cube?"

RETURN=$?
popd
exit $RETURN
