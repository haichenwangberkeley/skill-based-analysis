from pathlib import Path

from analysis.cli import build_parser
from analysis.config.load_summary import load_and_validate


def test_cli_parser_has_run():
    parser = build_parser()
    args = parser.parse_args(["run", "--summary", "a.json", "--inputs", "in", "--outputs", "out"])
    assert args.command == "run"


def test_summary_validation_structure():
    summary_path = Path("analysis/ATLAS_2012_H_to_gammagamma_discovery.analysis.json")
    normalized = load_and_validate(summary_path)
    assert "_inventory" in normalized
    assert normalized["_inventory"]["n_signal_regions"] >= 1
