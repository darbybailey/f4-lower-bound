# F4 Lower Bound — Standalone Certificate

**F4 > 4.4416832003**

This repository contains the standalone verification artifacts for the paper:

> McDonough, D. B. (2026). *F4 > 4.4416832003: Recurrent Digit Grammars and Certified Reciprocal Sums.* Certificate-only manuscript, version 1.2. Preprint. Published 2026-09-13. Version DOI: [10.5281/zenodo.24485654](https://doi.org/10.5281/zenodo.24485654). Concept DOI: [10.5281/zenodo.24485653](https://doi.org/10.5281/zenodo.24485653).

The paper PDF is in `paper/F4_Bound_Certificate_Paper.pdf`. The same verifier tree is also packaged as `F4-Certificate-Only-Standalone.zip`.

**Code: MIT License. Paper: CC BY 4.0.** Discovery software and search records are withheld. This repository contains only the mathematical witness and its verification software.

The published Zenodo record for the paper PDF and this certificate package is [10.5281/zenodo.24485654](https://zenodo.org/records/24485654) (version 1.2, published 2026-09-13). The concept DOI is [10.5281/zenodo.24485653](https://doi.org/10.5281/zenodo.24485653).

---

## Result

This package checks a particular explicit infinite four-term-arithmetic-progression-free
set A and proves F4 >= W(A) > 4.4416832003. It reproduces the exact rational
endpoints stored in `witness/weight_certificate.json`, with the conservative display

    4.4416832003495265335115002922388 < W(A)
                                     < 4.4416832003495265335115002922389.

The complete construction is supplied as both a finite root grammar and a
1,384-state ordinary base-55 digit DFA. The accepted input is n-1, read from its
least significant digit. `PROOF.md` explains the mathematical certificate.

## Boundary of disclosure

The public object is the mathematical witness and its verification software,
not the discovery engine. No optimizer, solver model, proposal generator,
screener, acquisition pipeline, candidate-pool archive, or harvest/search ledger
is included. The moment calculation is present only to verify the fixed witness.
Its mathematical role does not make its implementation commercially valueless:
the published proof methods and witness are intentionally disclosed.

Verification reproduces the correctness and weight of the supplied construction.
It does not reproduce its discovery, assess search efficiency, or establish that
any search was complete. Historic scan counts and experimental narratives are
not independently established by this package.

## Run the exact proof

From this repository root (or from the extracted certificate ZIP, which has the
same layout):

    python3 -O verify.py --output runs/verification.json

Python 3.10 or later (standard library) and a C++17 `g++` are required. `CXX` may
name another compatible compiler. The exact path uses no network, numerical
optimizer, NumPy, earlier ZIP, or external data. Successful results require
complete product-graph exhaustion; resource-limit termination is not acceptance.
The `runs/` directory contains generated output, not proof inputs, so repeat
runs do not invalidate the immutable-payload manifest. Output outside this
package is also supported.

The driver:

1. Checks the payload manifest and compiles the supplied grammar to the saved DFA.
2. Proves four-term freeness for all four entries by exact arithmetic-carry
   reachability. The respective complete closures are 801373, 801373, 801373,
   and 801382 states.
3. Recomputes the Walker baseline from its fixed digits, using exact finite-depth
   moments, directed rational rounding, and an explicit positive tail bound.
4. Recomputes the final infinite reciprocal enclosure at orders 8 and 10;
   requires nesting and exact equality with the stored order-10 endpoints.
5. Recompiles the supplied predecessor grammar, checks all its control entries,
   and recomputes its order-8 weight. The certified gain exceeds
   0.00000095439183802649. Stored baseline endpoints are expected outputs,
   not trusted premises.
6. Runs grammar/DFA membership controls, 52 small/constructed carry controls,
   72,000 compiler-control comparisons, and the deletion-1360 rejection control.

## Secondary checks

    python3 independent/run_checks.py --output runs/secondary.json

This runs the separately supplied carry implementation on the final DFA, after
validating its input format, 11-bit state bound, dead sink, and zero padding.
It is a cross-implementation control under the same carry formulation, not
external peer review. Original author attribution is not inferred from filenames.

An optional floating-point check uses a different decomposition:

    python3 independent/run_checks.py --with-floating --output runs/secondary.json

Only that optional check requires NumPy. Its floating agreement is not substituted
for the exact rational enclosure. Optional source files are retained unchanged;
the wrapper fixes the previously undocumented text-format conversion.

## Scope and provenance

`PROVENANCE.json` identifies the source archives and unchanged verification
modules. The predecessor archive chain is not shipped or needed. Its grammar
alone is included to reproduce the comparison result. No engine is nested in it.

The eight-insertion theorem from historical S15 is NOT replayed here. Its 4,008
dual certificates need an exhaustive subset-coverage certificate/checker as well
as the frozen baseline and primal feasibility proof. That is a separate result.
It must not be described as verified by this deposit. The same distinction applies
to other historical numerical exclusions not in this acceptance path.

There is no upper bound for arbitrary F4 sets, global optimum, finiteness proof,
5.1 proof, formal proof-assistant verification, peer-review claim, or literature
priority claim.

`validation/` contains recorded executions of this certificate and its secondary
checks. These are verification logs, not search logs, and are not proof premises.
The driver computes fresh results on every run. Recorded build timings and payload
counts describe their own run, not a guaranteed runtime on another machine.

## Checksums

See `SHA256SUMS.txt`. Verify with:

    sha256sum -c SHA256SUMS.txt

## License and Citation

Code: MIT License — see `LICENSE`.  
Paper: CC BY 4.0.

To cite: see `CITATION.cff`.

*Pip Projects, Inc. · Digital Sidewalk Lab · Independent Researcher*  
ORCID: [0000-0003-4072-6191](https://orcid.org/0000-0003-4072-6191)
