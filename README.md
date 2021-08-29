# Using PyInstaller with Github Actions

Example repo of using pyinstaller to create a desktop app.

## Cut out

I've cut the pypi_release section from the github action:

```
pypi_release:
  name: PyPi Release
  runs-on: [ubuntu-latest]
  steps:
  - uses: actions/checkout@v1
  - name: Set up Python 3.8
    uses: actions/setup-python@v2
    with:
      python-version: 3.8
  - name: Install dependencies
    run: |
      python -m pip install --upgrade pip
      pip install -r requirements.txt
  - name: PyPi - Build binary wheel and source tarball
    run: |
      python -m build --sdist --wheel --outdir dist/
  - name: PyPi - Publish to PyPI
    uses: pypa/gh-action-pypi-publish@master
    with:
      user: __token__
      password: ${{ secrets.PYPI_TOKEN }}
```

## Based on
- Original article: https://data-dive.com/multi-os-deployment-in-cloud-using-pyinstaller-and-github-actions
- Updated build.yml: https://raw.githubusercontent.com/mc51/Clipster-Desktop-Py/master/.github/workflows/build.yml
