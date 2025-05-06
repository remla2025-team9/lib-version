# lib-version

A lightweight Python utility library that provides a `VersionUtil` class for retrieving the current version of the package.  
It’s designed for reuse in other REMLA services such as `app-service`.

---

## Features

- Retrieves version from `__version__.py`
- Automatically updated using GitHub Actions and tags
- Can be installed via pip from GitHub

---

## Install

```bash
pip install git+https://github.com/remla2025-team9/lib-version.git@v1.0.0
```

---

## Use

```python
from lib_version.version_util import VersionUtil
print(VersionUtil.get_version())
```

or from terminal:

```bash
python lib_version/version_util.py
```

Quick check:

```bash
python test_version.py
```

---

## Integrate in Other Services

**Backend**:

```python
VersionUtil.get_version()
```

**Frontend**:

```javascript
fetch("/api/version")
  .then(res => res.json())
  .then(data => {
    document.getElementById("lib-version").textContent = `lib-version: ${data.lib_version}`;
  });
```

---

## Tagging a New Version

```bash
git tag v1.0.3
git push origin v1.0.3
```

This runs:
- `delivery.yml` to build and upload
- `ver.yml` to bump to next `-pre` version
