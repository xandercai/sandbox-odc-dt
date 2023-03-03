#!/bin/bash

# initialize database
echo "initialize open datacube..."
datacube -v system init

# add meta type to database
echo "add metadata samples: eo3_landsat_ard, eo3_sentinel_ard"
datacube metadata add https://explorer.sandbox.dea.ga.gov.au/metadata-types/eo3_landsat_ard.odc-type.yaml
datacube metadata add https://explorer.sandbox.dea.ga.gov.au/metadata-types/eo3_sentinel_ard.odc-type.yaml

# add product to database
echo "add product samples: ga_ls8c_ard_3, ga_s2am_ard_3"
datacube product add https://explorer.sandbox.dea.ga.gov.au/products/ga_ls8c_ard_3.odc-product.yaml
datacube product add https://explorer.sandbox.dea.ga.gov.au/products/ga_s2am_ard_3.odc-product.yaml
