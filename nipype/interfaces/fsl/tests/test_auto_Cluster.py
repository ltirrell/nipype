# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.fsl.model import Cluster
def test_Cluster_inputs():
    input_map = dict(dlh=dict(argstr='--dlh=%.10f',
    ),
    num_maxima=dict(argstr='--num=%d',
    ),
    cope_file=dict(argstr='--cope=%s',
    ),
    pthreshold=dict(requires=['dlh', 'volume'],
    argstr='--pthresh=%.10f',
    ),
    out_index_file=dict(hash_files=False,
    argstr='--oindex=%s',
    ),
    threshold=dict(mandatory=True,
    argstr='--thresh=%.10f',
    ),
    out_mean_file=dict(hash_files=False,
    argstr='--omean=%s',
    ),
    find_min=dict(),
    std_space_file=dict(argstr='--stdvol=%s',
    ),
    out_localmax_txt_file=dict(hash_files=False,
    argstr='--olmax=%s',
    ),
    out_localmax_vol_file=dict(hash_files=False,
    argstr='--olmaxim=%s',
    ),
    in_file=dict(mandatory=True,
    argstr='--in=%s',
    ),
    fractional=dict(),
    out_pval_file=dict(hash_files=False,
    argstr='--opvals=%s',
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    use_mm=dict(),
    minclustersize=dict(argstr='--minclustersize',
    ),
    no_table=dict(),
    warpfield_file=dict(argstr='--warpvol=%s',
    ),
    args=dict(argstr='%s',
    ),
    volume=dict(argstr='--volume=%d',
    ),
    connectivity=dict(argstr='--connectivity=%d',
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    out_max_file=dict(hash_files=False,
    argstr='--omax=%s',
    ),
    output_type=dict(),
    xfm_file=dict(argstr='--xfm=%s',
    ),
    peak_distance=dict(argstr='--peakdist=%.10f',
    ),
    out_threshold_file=dict(hash_files=False,
    argstr='--othresh=%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    out_size_file=dict(hash_files=False,
    argstr='--osize=%s',
    ),
    )
    inputs = Cluster.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value
def test_Cluster_outputs():
    output_map = dict(threshold_file=dict(),
    localmax_vol_file=dict(),
    size_file=dict(),
    mean_file=dict(),
    max_file=dict(),
    pval_file=dict(),
    localmax_txt_file=dict(),
    index_file=dict(),
    )
    outputs = Cluster.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value