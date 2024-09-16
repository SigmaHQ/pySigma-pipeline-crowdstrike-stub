from sigma.backends.crowdstrike import LogScaleBackend
from sigma.pipelines.crowdstrike import (
    crowdstrike_fdr_pipeline,
    crowdstrike_falcon_pipeline,
)

def test_backend_logscale():
    assert LogScaleBackend()

def test_pipeline_fdr():
    assert crowdstrike_fdr_pipeline()

def test_pipeline_falcon():
    assert crowdstrike_falcon_pipeline()