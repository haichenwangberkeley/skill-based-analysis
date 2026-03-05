from analysis.samples.strategy import build_parser


def test_strategy_parser():
    parser = build_parser()
    args = parser.parse_args([
        "--registry",
        "r.json",
        "--regions",
        "regions.yaml",
        "--summary",
        "s.json",
        "--out",
        "o.json",
    ])
    assert args.registry == "r.json"
    assert args.regions == "regions.yaml"
    assert args.out == "o.json"
