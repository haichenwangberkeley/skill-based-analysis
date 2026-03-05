from analysis.plotting.blinded_regions import build_parser


def test_blinded_regions_parser():
    parser = build_parser()
    args = parser.parse_args([
        "--outputs",
        "outputs",
        "--registry",
        "r.json",
        "--regions",
        "regions.yaml",
        "--fit-id",
        "FIT_MAIN",
    ])
    assert args.outputs == "outputs"
    assert args.fit_id == "FIT_MAIN"
    assert args.unblind_sr is False
