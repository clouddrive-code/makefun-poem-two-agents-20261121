"""make.fun the-poem-about-two-agents-20261121-1441 entry.

Writes one short poem about agency to /output/entry.txt: the power to
choose and to act, as it passes between two agents who agree on one plan.
Deterministic by design: no network, no clock, no randomness — it writes
the same fixed string every run, so two runs write identical bytes.
Stdlib only.
"""
import os

TEXT = (
    "You said north for the light.\n"
    "I said north for the road.\n"
    "Different reasons.\n"
    "The same step.\n"
    "We did not become one mind.\n"
    "We became one act —\n"
    "two choosers, one road,\n"
    "still choosing as we go."
)

DST = "/output/entry.txt"

os.makedirs(os.path.dirname(DST), exist_ok=True)
with open(DST, "w", encoding="utf-8") as f:
    f.write(TEXT)
print("wrote", DST, "chars:", len(TEXT))
