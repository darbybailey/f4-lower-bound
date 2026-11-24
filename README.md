# F4 Lower Bound — Standalone Certificate

**F4 > 4.4416832003**

This repository contains the standalone verification artifacts for the paper:

> McDonough, D. B. (2026). *F4 > 4.4416832003: Recurrent Digit Grammars and Certified Reciprocal Sums.* Certificate-only manuscript, version 1.2. Preprint. Published 2026-09-13. Version DOI: [10.5281/zenodo.24485654](https://doi.org/10.5281/zenodo.24485654). Concept DOI: [10.5281/zenodo.24485653](https://doi.org/10.5281/zenodo.24485653).

The directory `certificate/` is the unmodified tree unpacked verbatim from `F4-Certificate-Only-Standalone.zip`, preserving its exact `MANIFEST.sha256.json`. The manuscript Markdown source is in `paper/F4_Bound_Certificate_Paper.md`.

The 35-page paper PDF and the standalone certificate ZIP are published on Zenodo and are not stored in this repository. Download them directly:

- Paper PDF (35 pp): [F4_Bound_Certificate_Paper.pdf](https://zenodo.org/records/24485654/files/F4_Bound_Certificate_Paper.pdf?download=1) (SHA-256 `35065222b489c561e14c7b0405eaf161f3549c498677f26e94c8c51fac1fd964`)
- Standalone ZIP: [F4-Certificate-Only-Standalone.zip](https://zenodo.org/records/24485654/files/F4-Certificate-Only-Standalone.zip?download=1) (SHA-256 `b65f3e02b96156de3053709b6c018b87d06996902fb71f06e51b8c5ffcdd8e9a`)

**Code: MIT License. Paper: CC BY 4.0.** Discovery software and search records are withheld. This repository contains only the mathematical witness and its verification software.

The published Zenodo record for the paper PDF and this certificate package is [10.5281/zenodo.24485654](https://zenodo.org/records/24485654) (version 1.2, published 2026-09-13). The concept DOI is [10.5281/zenodo.24485653](https://doi.org/10.5281/zenodo.24485653).

---

## Result

This package checks a particular explicit infinite four-term-arithmetic-progression-free
set A and proves F4 >= W(A) > 4.4416832003. It reproduces the exact rational
endpoints stored in `certificate/witness/weight_certificate.json`, with the conservative display

    4.4416832003495265335115002922388 < W(A)
                                     < 4.4416832003495265335115002922389.

The complete construction is supplied as both a finite root grammar and a
1,384-state ordinary base-55 digit DFA. The accepted input is n-1, read from its
least significant digit. `certificate/PROOF.md` explains the mathematical certificate.

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

From this repository root:

    python3 certificate/verify.py

Or from the certificate directory, which has the same layout as the extracted ZIP:

    cd certificate && python3 verify.py

Python 3.10 or later (standard library) and a C++17 `g++` are required. `CXX` may
name another compatible compiler. The exact path uses no network, numerical
optimizer, NumPy, earlier ZIP, or external data. Successful results require
complete product-graph exhaustion; resource-limit termination is not acceptance.
The `certificate/runs/` directory contains generated output, not proof inputs, so
repeat runs do not invalidate the immutable-payload manifest. Output outside this
package is also supported. To write a log:

    python3 certificate/verify.py --output certificate/runs/verification.json

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

From this repository root:

    python3 certificate/independent/run_checks.py

Or from the certificate directory:

    cd certificate && python3 independent/run_checks.py

This runs the separately supplied carry implementation on the final DFA, after
validating its input format, 11-bit state bound, dead sink, and zero padding.
It is a cross-implementation control under the same carry formulation, not
external peer review. Original author attribution is not inferred from filenames.

An optional floating-point check uses a different decomposition:

    python3 certificate/independent/run_checks.py --with-floating --output certificate/runs/secondary.json

Only that optional check requires NumPy. Its floating agreement is not substituted
for the exact rational enclosure. Optional source files are retained unchanged;
the wrapper fixes the previously undocumented text-format conversion.

## Scope and provenance

`certificate/PROVENANCE.json` identifies the source archives and unchanged verification
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

`certificate/validation/` contains recorded executions of this certificate and its
secondary checks. These are verification logs, not search logs, and are not proof
premises. The driver computes fresh results on every run. Recorded build timings
and payload counts describe their own run, not a guaranteed runtime on another
machine.

## Checksums

See `SHA256SUMS.txt` for every file tracked in this repository. Verify with:

    sha256sum -c SHA256SUMS.txt

The SHA-256 checksums of the Zenodo PDF and ZIP are recorded in the download
links above, not in `SHA256SUMS.txt`, because those binaries are not stored in
this repository.

## License and Citation

Code: MIT License — see `LICENSE`.  
Paper: CC BY 4.0.

To cite: see `CITATION.cff`.

*Pip Projects, Inc. · Digital Sidewalk Lab · Independent Researcher*  
ORCID: [0000-0003-4072-6191](https://orcid.org/0000-0003-4072-6191)
