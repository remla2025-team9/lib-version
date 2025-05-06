# lib-version

A lightweight Python utility library developed for the REMLA course. It provides a way to retrieve the current version of the package using a `VersionUtil` class.

This library is intended to be used across other services like `app-service` to expose consistent versioning information, useful in logs, debugging, and UI.

---

## Features

- `VersionUtil.get_version()` returns the current version as defined in `__version__.py`
- Version string is automatically updated via GitHub Actions (`delivery.yml` and `ver.yml`)
- Git tags and pre-release bumps are handled using semantic versioning
- Distributed as a Python package with both `sdist` and `wheel` builds

---

## How to Use

```python
from lib_version.version_util import VersionUtil

print(VersionUtil.get_version())
```

Or run directly from the terminal:

```bash
python lib_version/version_util.py
```

---

## How to Check the Version

You can also run the following script to check the current version:

```bash
python test_version.py
```

It will print something like:

```
Library Version: 1.0.4-pre
```

---

## Triggering a New Version

To tag and bump a new version:

```bash
git tag v1.0.3
git push origin v1.0.3
```

This will:
- Run the `delivery.yml` workflow to build and upload the Python package
- Run the `ver.yml` workflow to bump the version on `main` to something like `1.0.4-pre`
