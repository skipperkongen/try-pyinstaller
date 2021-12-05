# Using PyInstaller with Github Actions

This repo shows you how to use pyinstaller to build and release a Python desktop app.
The build script is based on the [Clipster Desktop](https://github.com/mc51/Clipster-Desktop)
project on Github.

You can use this project as a template for your own desktop app.

## About this desktop app

I have created a minimal example of a desktop app. The app uses tkinter and requests to
display a random acronym from the 80's.

## How to use it

These are the steps to use this project as the basis for your own desktop app.

1. Replace the code in `cli.py` and `acronyms` folder with your own
1. Replace the icons in `resources` with your own
1. Edit `.github/workflows/build.yml` and change the name "acronyms" to the name of your app


To create a new release, use this git command:

```
git tag v0.0.1 master  # pick a version that has not been used
git push origin v0.0.1
```

## Creating icon files

Your original icon file (.png) should by 512x512 pixels. Use whatever design you
want. From this you will create two icon-files, for Windows and Mac OS respectively:
- application.ico (256x256) (Windows)
- application.icns (?x?) (Mac Os)

You can use the online tool [cloudconvert.com](https://cloudconvert.com/png-to-icns)
to create a both .ico and .icns file from your .png file. If you get an error,
try to first convert the size of your input image to dimensions 512x512.

## Cut out

I've cut the pypi_release section from the original github action yml, because
I don't feel the need to release the desk top app on PyPi. However, this is
the section I cut out:

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
