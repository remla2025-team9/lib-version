# lib-version

A Python utility library that provides a `VersionUtil` class for retrieving the current version of the package.  
This library is intended for reuse across other services like `app-service`.

---

## Features

- Provides a simple interface to retrieve package version
- Version is stored in the `lib_version/version.py` file
- Versioning is managed automatically through GitHub Actions workflows
- Follows semantic versioning with stable and pre-release versions

---

## Install

```bash
pip install git+https://github.com/remla2025-team9/lib-version.git@v0.0.1
```

Replace `v0.0.1` with the desired version tag.

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
from flask import Flask, jsonify
from lib_version.version_util import VersionUtil

app = Flask(__name__)

@app.route("/api/version")
def get_lib_version():
    return jsonify({"lib_version": VersionUtil.get_version()})
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

## Versioning System

We've chosen to implement automatic versioning with a manual trigger for releases, providing both continuous delivery and controlled releases.

### Overview

The library uses two automated workflows to manage versioning:
1. **Delivery workflow**: Runs on pushes to main branch, creates pre-release versions
2. **Release workflow**: Manually triggered, creates stable releases

All version numbers follow [Semantic Versioning](https://semver.org/) with the format:
- Stable releases: `MAJOR.MINOR.PATCH` (e.g., `2.0.0`)
- Pre-releases: `MAJOR.MINOR.PATCH-pre-N` (e.g., `2.0.1-pre-0`)

### Versioning Process

#### Daily Development (Pre-releases)

1. When commits are pushed to the `main` branch, the `delivery.yml` workflow runs automatically
2. The workflow:
   - Identifies the latest pre-release version or stable version
   - Increments the pre-release counter or creates a new pre-release
   - Updates `lib_version/version.py` with the new version
   - Creates a Git tag with the new version
   - Pushes the changes and tag to the repository

#### Creating Stable Releases

1. Manually trigger the `release.yml` workflow from GitHub Actions UI
2. Select the version bump level: `patch`, `minor`, or `major`
3. The workflow:
   - Identifies the latest stable version
   - Bumps the version according to selected level
   - Updates `lib_version/version.py` with the stable version
   - Creates a Git tag for the stable release
   - Creates a GitHub Release
   - Immediately creates a new pre-release version for continued development
   - Updates `lib_version/version.py` again with the pre-release version
   - Creates a Git tag for the pre-release
   - Pushes all changes and tags to the repository

### Version Determination Logic

- **Stable releases**: Found by filtering Git tags matching `v*.*.*` pattern and excluding `-pre-` tags
- **Pre-releases**: Found by searching Git tags matching `v*-pre-*` pattern
- Git tags are the source of truth for all version information

---
