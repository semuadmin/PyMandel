# How to contribute

Here are some guidelines on how to contribute to the PyMandel project.

We appreciate any contribution, from fixing a grammar mistake in a comment to implementing new functionality. Please read this section if you are contributing your work.

Being one of our contributors, you agree and confirm that:

* The work is all your own. For the avoidance of doubt, this means **no AI coding agents such as Copilot**.
* Your work will be distributed under a BSD 3-Clause License once your pull request is merged.
* You submitted work fulfils or mostly fulfils our styles and standards.

Please help us keep our issue list small by adding fixes: #{$ISSUE_NO} to the commit message of pull requests that resolve open issues. GitHub will use this tag to auto close the issue when the PR is merged.

## Coding conventions

* This is open source software. We endeavour to make the code as transparent as possible. Favour clarity over brevity.
* We use and recommend [Visual Studio Code](https://code.visualstudio.com/) with the [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) for development and testing.
* Code should be documented in accordance with [Sphinx](https://www.sphinx-doc.org/en/master/) docstring conventions.
* Code should formatted using [black](https://pypi.org/project/black/) (>= 20.8).
* We use and recommend [pylint](https://pypi.org/project/pylint/) (>=2.6.0) for code analysis.
* We use and recommend [bandit](https://pypi.org/project/bandit/) (>=1.7) for security vulnerability analysis.
* Commits should be [signed](https://docs.github.com/en/authentication/managing-commit-signature-verification/signing-commits).
* PyMandel uses [Numba](http://numba.pydata.org/) for JIT compilation, parallelisation and caching. This affords very significant
performance enhancements over native interpreted Python, but does necessitate certain coding constraints in the affected module(s) (`mandlebrot.py`) - refer to the Numba documentation for further details.

## Testing

We use python's native pytest framework for local unit testing, complemented by the Github Actions automated build and testing workflow. Code coverage is extremely limited at present so we welcome improvements.

Please write pytest examples for new code you create and add them to the /tests folder following the naming convention test_*.py.

We test on the following platforms:
* Windows 11
* MacOS 26/27
* Linux 24/26
* Raspberry Pi OS Trixie

## Submitting changes

Please send a [GitHub Pull Request to PyMandel](https://github.com/semuconsulting/PyMandel/pulls) with a clear list of what you've done (read more about [pull requests](https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/about-pull-requests)). Please follow our coding conventions (below) and make sure all of your commits are atomic (one feature per commit).

Always write a clear log message for your commits. One-line messages are fine for small changes, but bigger changes should look like this:

    $ git commit -m "A brief summary of the commit
    > 
    > A paragraph describing what changed and its impact."

Please use the supplied [Pull Request Template](https://github.com/semuconsulting/pymandel/blob/master/.github/pull_request_template.md).

Please sign all commits - see [Signing GitHub Commits](https://docs.github.com/en/authentication/managing-commit-signature-verification/signing-commits) for instructions.


Thanks,

semuadmin