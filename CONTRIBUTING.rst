.. highlight:: shell

============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways to any of the packages that are included in HyRiver
project. The workflow is the same for all packages. In this page, a contribution workflow
for `PyGridMET <https://github.com/cheginit/pygridmet>`__ is explained. You can easily
adapt it to other packages by replacing ``pygridmet`` with the name of the package
that you want to contribute to.

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/hyriver/pygridmet/issues.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Other than new features that you might have in mind, you can look through
the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

PyGridMET could always use more documentation, whether as part of the
official PyGridMET docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/hyriver/pygridmet/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up pygridmet for local development.

1. Fork the PyGridMET repo through the GitHub website.
2. Clone your fork locally and add the main ``pygridmet`` as the upstream remote:

.. code-block:: console

    $ git clone git@github.com:your_name_here/pygridmet.git
    $ git remote add upstream git@github.com:hyriver/pygridmet.git

3. Install your local copy into a virtualenv. Assuming you have ``mamba`` installed,
   this is how you can set up your fork for local development:

.. code-block:: console

    $ cd pygridmet/
    $ mamba env create -f ci/requirements/environment-dev.yml
    $ mamba activate pygridmet-dev
    $ python -m pip install . --no-deps

4. Create a branch for local development:

.. code-block:: console

    $ git checkout -b bugfix-or-feature/name-of-your-bugfix-or-feature
    $ git push

5. Now you can make your changes locally, make sure to add a description of
   the changes to ``HISTORY.rst`` file and add extra tests, if applicable,
   to ``tests`` folder. Also, make sure to give yourself credit by adding
   your name at the end of the item(s) that you add in the history like this
   ``By `Taher Chegini <https://github.com/hyriver>`_``. Then,
   fetch the latest updates from the remote and resolve any merge conflicts:

.. code-block:: console

    $ git fetch upstream
    $ git merge upstream/name-of-your-branch

6. Then create a new environment for linting and another for testing:

.. code-block:: console

    $ mamba create -n py11 python=3.11 nox tomli pre-commit codespell gdal
    $ mamba activate py11
    $ nox -s pre-commit
    $ nox -s type-check

    $ mamba create -n py38 python=3.8 nox tomli pre-commit codespell gdal
    $ mamba activate py38
    $ nox -s tests

   Note that if Python 3.11 is already installed on your system, you can
   skip creating the ``py11`` environment and just use your system's Python 3.11
   to run the linting and type-checking tests, like this:

.. code-block:: console

    $ mamba create -n py38 python=3.8 nox tomli pre-commit codespell gdal
    $ mamba activate py38
    $ nox

7. If you are making breaking changes make sure to reflect them in
   the documentation, ``README.rst``, and tests if necessary.

8. Commit your changes and push your branch to GitHub. Start the commit message with
   ``ENH:``, ``BUG:``, ``DOC:`` to indicate whether the commit is a new feature,
   documentation related, or a bug fix. For example:

.. code-block:: console

    $ git add .
    $ git commit -m "ENH: A detailed description of your changes."
    $ git push origin name-of-your-branch

9. Submit a pull request through the GitHub website.

Tips
----

To run a subset of tests:

.. code-block:: console

    $ nox -s tests -- -n=1 -k "test_name1 or test_name2"

Deploying
---------

A reminder for the maintainers on how to deploy.
Make sure all your changes are committed (including an entry in HISTORY.rst).
Then run:

.. code-block:: console

    $ git tag -a vX.X.X -m "vX.X.X"
    $ git push --follow-tags

where ``X.X.X`` is the version number following the
`semantic versioning spec <https://semver.org>`__ i.e., MAJOR.MINOR.PATCH.
Then release the tag from Github and Github Actions will deploy it to PyPi.
