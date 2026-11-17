<h1 align="center">Synthetic Humanism</h1>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT%20%2F%20Apache--2.0-blue.svg" alt="License: MIT / Apache-2.0"></a>
  <a href="https://github.com/Dirgha-AI/synthetic-humanism/actions/workflows/ci.yml"><img src="https://github.com/Dirgha-AI/synthetic-humanism/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://github.com/Dirgha-AI/ahimsa-ai"><img src="https://img.shields.io/badge/stage%201-AIA%20v1.1-teal.svg" alt="Stage 1: AIA v1.1"></a>
  <a href="https://github.com/Dirgha-AI/lokahi"><img src="https://img.shields.io/badge/stage%202-LOKAHI%20v0.1.3-purple.svg" alt="Stage 2: LOKAHI v0.1.3"></a>
</p>

<p align="center"><strong>"Intelligence, biological or synthetic, shall strive to cause no harm. Synthetic humanism applies intelligence toward the ahimsa of abundance."</strong></p>

Synthetic Humanism is a framework for building AI around one rule: cause no harm (*ahimsa*), and use what machines produce to widen shared abundance. This repository holds the manifesto, the essays and talks behind it, and a working two-stage check that turns the rule into software.

**Status:** v0.1.0, work in progress. The code runs and is tested, but the framework hasn't been independently reviewed. The [known limits](#known-limits) say what the results do and don't show.

## The idea in four parts

1. **Intelligence as one continuous project.** People and machines both take part in reducing suffering that nobody chose. Humans stay accountable for what machines do.
2. **From Asimov's laws to one rule.** Asimov's Three Laws fail in his own stories: robots deadlock, overrule people for their own good, or tell comforting lies. The manifesto derives physical safety, a duty of care, non-extraction and shared flourishing from a single non-harm rule instead.
3. **Economics after the wage.** If machines do more of the work, public revenue can't rest on payroll taxes. The manifesto proposes four non-labour revenue sources and Universal Basic Capital, and the [simulator](02_COMPUTATIONAL_ENGINE/macro/sim_abundance_macro.py) runs three fiscal scenarios.
4. **A two-stage check in code.**
   - **Stage 1, before deployment:** [Ahimsa AI](https://github.com/Dirgha-AI/ahimsa-ai) (AIA v1.1) scores a project on risk of harm and on public benefit, refuses five red-line uses outright, and compiles approved projects into signed boundary manifests.
   - **Stage 2, at runtime:** [LOKAHI](https://github.com/Dirgha-AI/lokahi) checks each agent tool call against the signed manifest. Irreversible actions need separate people to say yes. If nobody answers in time, the answer is no.

Read the [manifesto](01_MANIFESTO/Synthetic-Humanism-Manifesto.md) for the full argument.

## Try it

Python 3.10 or later, no dependencies:

```bash
git clone https://github.com/Dirgha-AI/synthetic-humanism.git
cd synthetic-humanism

python 02_COMPUTATIONAL_ENGINE/validate_schema.py                    # schema check on 50 systems and both examples
python 02_COMPUTATIONAL_ENGINE/tests/test_scorer.py                  # 13 Stage 1 unit tests
python 02_COMPUTATIONAL_ENGINE/benchmark/run_benchmark.py            # 50 systems, 1,000-trial sensitivity check
python 02_COMPUTATIONAL_ENGINE/benchmark/run_historical_disasters.py # both stages on 20 documented failures
python 02_COMPUTATIONAL_ENGINE/macro/sim_abundance_macro.py          # fiscal scenarios
python 02_COMPUTATIONAL_ENGINE/lokahi/tests/test_core.py             # 70 Stage 2 unit tests
```

## Results so far

- **50-system benchmark.** AIA v1.1 refuses 14 of 50 example systems (28%) across agriculture, finance, health, defence and public administration. With every weight shifted by up to 25% over 1,000 trials, 98.57% of refuse-or-allow decisions stay the same.
- **20 documented failures.** The benchmark rebuilds 20 real AI and automation failures, among them Robodebt, the Dutch childcare benefits scandal, Knight Capital and the UK Post Office Horizon scandal. Stage 1 would have refused 10 before deployment. Stage 2 would have stopped the other 10 at runtime.

## Known limits

1. **We wrote the cases.** The 50 systems and the 20 failure reconstructions were written by the authors, with the expected answer known in advance. Catching all 20 shows the two stages behave as designed on those cases. It doesn't predict field performance.
2. **Self-reported inputs.** Stage 1 scores what a project declares about itself. The `--strict-floor` option raises declared risk to what the scorer infers, but it can't catch a false declaration.
3. **Stage 2 limits apply.** LOKAHI v0.1.3 uses shared-secret signatures and hasn't had a security review. See its [known limits](https://github.com/Dirgha-AI/lokahi#known-limits).
4. **The economics are a model.** The fiscal simulator uses stated assumptions and isn't a forecast.

## Repository layout

| Path | What it contains |
|---|---|
| [`01_MANIFESTO/`](01_MANIFESTO/) | The manifesto, in Markdown and as a web page |
| [`02_COMPUTATIONAL_ENGINE/scorer/`](02_COMPUTATIONAL_ENGINE/scorer/) | Stage 1 scorer and manifest compiler (AIA v1.1), with an approved and a refused example |
| [`02_COMPUTATIONAL_ENGINE/schema/`](02_COMPUTATIONAL_ENGINE/schema/) | JSON Schema for project declarations and manifests |
| [`02_COMPUTATIONAL_ENGINE/benchmark/`](02_COMPUTATIONAL_ENGINE/benchmark/) | 50-system benchmark and the 20 failure reconstructions |
| [`02_COMPUTATIONAL_ENGINE/macro/`](02_COMPUTATIONAL_ENGINE/macro/) | Fiscal simulator and its results |
| [`02_COMPUTATIONAL_ENGINE/lokahi/`](02_COMPUTATIONAL_ENGINE/lokahi/) | A copy of LOKAHI v0.1.3 so the benchmark runs from one clone. The [LOKAHI repository](https://github.com/Dirgha-AI/lokahi) is the source of truth |
| [`02_COMPUTATIONAL_ENGINE/refusal_list.yaml`](02_COMPUTATIONAL_ENGINE/refusal_list.yaml) | The five red lines and the score bands |
| [`03_REFERENCE_CORPUS/bib/`](03_REFERENCE_CORPUS/bib/) | Bibliography |
| [`04_AUTHOR_CANON/`](04_AUTHOR_CANON/) | Essays, a TEDx talk transcript and video subtitles |
| [`CHANGELOG.md`](CHANGELOG.md) | What changed in each release |

## Related projects

- [**LOKAHI**](https://github.com/Dirgha-AI/lokahi): the runtime gate for agent tool calls (Stage 2).
- [**Ahimsa AI**](https://github.com/Dirgha-AI/ahimsa-ai): the design-time impact assessment, as a standalone package (Stage 1).

## Author

**Salik Shah**, Dirgha AI and *Mithila Review*, New Delhi ([salikshah.com](https://salikshah.com), [x.com/salik](https://x.com/salik), [GitHub](https://github.com/salikshah)). LOKAHI's security architecture is by Sabin Ranjit.

## Citation

See [`CITATION.cff`](CITATION.cff), or:

```bibtex
@software{shah2026synthetichumanism,
  author  = {Shah, Salik},
  title   = {Synthetic Humanism: Intelligence, Non-Harm, and the Ahimsa of Abundance},
  version = {0.1.0},
  year    = {2026},
  url     = {https://github.com/Dirgha-AI/synthetic-humanism}
}
```

## License

The manifesto, essays and Stage 1 code are licensed under [MIT](LICENSE). The LOKAHI copy is licensed under [Apache-2.0](02_COMPUTATIONAL_ENGINE/lokahi/LICENSE), and its scenario set under [CC BY 4.0](02_COMPUTATIONAL_ENGINE/lokahi/data/LICENSE).
