# Reproducibility

Requires Python 3.10 or newer and no third-party packages.

Run the complete small verification suite:

```bash
python run_checks.py
```

Generate a trajectory summary without printing enormous integers:

```bash
python tools/trajectory_report.py --X 5 --n0 7 --steps 10000
```

Verify a rigorously controlled finite-growth block:

```bash
python tools/verify_finite_growth_block.py --m 20 --L 50
```

Trajectory reports are experimental evidence only. The finite-growth checker verifies an exact finite identity, not infinite divergence.
