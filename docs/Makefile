# Makefile for Sphinx documentation

SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = kALDoExamples
SOURCEDIR     = .
BUILDDIR      = _build

help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile html clean

# Build HTML documentation (runs setup first)
html:
	@python3 setup_docs.py
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Clean build artifacts
clean:
	@rm -rf $(BUILDDIR)
	@rm -rf docsource/density_functional_theory
	@rm -rf docsource/empirical_potentials
	@rm -rf docsource/machine_learning_potentials

# Other targets
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
