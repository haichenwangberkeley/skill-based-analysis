from analysis.stats.mass_model_selection import build_parser


def test_mass_model_selection_parser():
    parser = build_parser()
    args = parser.parse_args([
        "--fit-id",
        "FIT1",
        "--summary",
        "s.json",
        "--hists",
        "h",
        "--strategy",
        "st.json",
        "--out",
        "o.json",
    ])
    assert args.fit_id == "FIT1"
