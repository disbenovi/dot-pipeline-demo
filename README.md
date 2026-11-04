# dot-pipeline-demo

A deliberately small repository used to prove one chain end to end:

```
Gitea issue labelled "dot"
  -> n8n mirrors it to a GitHub issue
  -> the Dot picks it up, builds in its own cloud computer, returns a patch
  -> a Codex task applies the patch, pushes a branch, opens a draft PR
  -> the host lands those same commits on Gitea and opens the PR that counts
  -> merge on Gitea, mirror carries main back to GitHub
```

Nothing here is production code. It exists so the pipeline can be debugged on
something where a mistake costs nothing.

## Layout

| Path | Purpose |
|---|---|
| `greet.py` | the only module, small enough to change in one patch |
| `tests/test_greet.py` | its tests, run with `python3 -m unittest discover -s tests` |
| `AGENTS.md` | the contract a Dot reads before working |

## Running the tests

```
python3 -B -m unittest discover -s tests -v
```
