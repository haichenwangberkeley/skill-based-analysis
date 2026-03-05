import argparse
from pathlib import Path
from typing import Any, Dict

import numpy as np
import pyhf

from analysis.common import ensure_dir, read_json, write_json



def run_fit(workspace_path: Path) -> Dict[str, Any]:
    ws_spec = read_json(workspace_path)
    ws = pyhf.Workspace(ws_spec)
    model = ws.model()
    data = ws.data(model)
    poi_name = model.config.poi_name

    try:
        bestfit, twice_nll = pyhf.infer.mle.fit(data, model, return_fitted_val=True)
        bestfit = np.asarray(bestfit, dtype=float)

        poi_idx = model.config.poi_index
        poi_hat = float(bestfit[poi_idx])

        return {
            "poi_name": poi_name,
            "bestfit_poi": poi_hat,
            "bestfit_all": bestfit.tolist(),
            "twice_nll": float(twice_nll),
            "status": "ok",
            "n_pars": int(len(bestfit)),
        }
    except Exception as exc:
        # Keep pipeline executable and emit actionable diagnostics.
        return {
            "poi_name": poi_name,
            "bestfit_poi": 1.0,
            "bestfit_all": [],
            "twice_nll": None,
            "status": "failed",
            "error": str(exc),
            "n_pars": int(len(model.config.par_names)),
        }



def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run pyhf fit")
    parser.add_argument("--workspace", required=True)
    parser.add_argument("--fit-id", required=True)
    parser.add_argument("--out", required=True)
    return parser



def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    result = run_fit(Path(args.workspace))
    result["fit_id"] = args.fit_id

    out_path = Path(args.out)
    ensure_dir(out_path.parent)
    write_json(out_path, result)

    print("fit {} status={} poi({})={:.6g}".format(args.fit_id, result["status"], result["poi_name"], result["bestfit_poi"]))


if __name__ == "__main__":
    main()
