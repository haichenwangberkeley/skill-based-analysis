from pathlib import Path

from analysis.partitioning.build_partitions import build_parser, build_partitions


def test_partitioning_parser():
    parser = build_parser()
    args = parser.parse_args(
        [
            "--categories",
            "analysis/categories.yaml",
            "--regions",
            "analysis/regions.yaml",
            "--out-spec",
            "spec.json",
            "--out-manifest",
            "manifest.json",
            "--out-checks",
            "checks.json",
        ]
    )
    assert args.categories == "analysis/categories.yaml"
    assert args.regions == "analysis/regions.yaml"
    assert args.out_spec == "spec.json"


def test_partition_build(tmp_path: Path):
    out_spec = tmp_path / "partition_spec.json"
    out_manifest = tmp_path / "partitions.json"
    out_checks = tmp_path / "partition_checks.json"

    checks = build_partitions(
        categories_path=Path("analysis/categories.yaml"),
        regions_path=Path("analysis/regions.yaml"),
        out_spec=out_spec,
        out_manifest=out_manifest,
        out_checks=out_checks,
    )

    assert out_spec.exists()
    assert out_manifest.exists()
    assert out_checks.exists()
    assert checks["summary"]["status"] == "pass"
    assert checks["meta"]["n_categories"] >= 1
    assert checks["meta"]["n_partitions"] >= 1

