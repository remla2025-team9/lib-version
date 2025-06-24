# Lib-Version Library

A Python utility library that provides a `VersionUtil` class for retrieving the current version of the package.  
This library is intended for reuse across other services like `app-service`.

---

## Features

- Provides a simple interface to retrieve package version
- Version is stored in the `lib_version/__version__.py` file
- Versioning is managed automatically through GitHub Actions workflows
- Follows semantic versioning with stable and pre-release versions

--- 

## Test the library

Requirements:
- Python 3.9 or higher 

The library can be tested from this repository by executing the following command:

```bash
python -m lib_version.version_util
```

---

## How to install the library

```bash
pip install git+https://github.com/remla2025-team9/lib-version.git@v1.0.0
```

Replace `v1.0.0` with the desired version tag.

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
- Stable releases: `MAJOR.MINOR.PATCH` (e.g., `1.0.1`)
- Pre-releases: `MAJOR.MINOR.PATCH-pre-N` (e.g., `1.0.2-pre-1`)

### Versioning Process

#### Daily Development (Pre-releases)

1. When commits are pushed to the `main` branch, the `delivery.yml` workflow runs automatically
2. The workflow:
   - Finds the latest pre-release version or stable version  
   - Increments the pre-release counter (e.g., `-pre-1` to `-pre-2`) or creates the first pre-release for a new version
   - Updates `lib_version/__version__.py` with the new version
   - Creates a Git tag with the new version (e.g., `v1.0.2-pre-1`)
   - Commits and pushes the changes and tag to the repository

#### Creating Stable Releases

1. Manually trigger the `release.yml` workflow from GitHub Actions UI
2. Select the version bump level: `patch`, `minor`, or `major`
3. The workflow:
   - Finds the latest stable version (excluding pre-releases)
   - Bumps the version according to selected level
   - Updates `lib_version/__version__.py` with the stable version
   - Creates a Git tag for the stable release (e.g., `v1.0.2`)
   - Creates a GitHub Release with release notes
   - Immediately prepares for next development cycle:
     - Creates a new pre-release version (patch + 1 with `-pre-1`)
     - Updates `lib_version/__version__.py` again with the pre-release version
     - Creates a Git tag for the pre-release (e.g., `v1.0.3-pre-1`)
   - Commits and pushes all changes and tags to the repository

### Version Determination Logic

- **Stable releases**: Found by filtering Git tags matching `v*.*.*` pattern and excluding tags containing `-pre-`
- **Pre-releases**: Found by searching Git tags matching `v*-pre-*` pattern  
- **Source of truth**: Git tags are the authoritative source for all version information
- **Automatic sync**: The `__version__.py` file is automatically updated by workflows to match the Git tags

---

## Manual Intervention

The automated workflows handle all versioning needs. However, for troubleshooting:

1. **View current version**:
   ```bash
   cat lib_version/__version__.py
   ```

2. **List all version tags**:
   ```bash
   git tag -l 'v*.*.*' | sort -V
   ```

3. **List pre-release tags**:
   ```bash
   git tag -l 'v*-pre-*' | sort -V
   ```

4. **Manually trigger a release**:
   - Go to GitHub repository → Actions → "Release" workflow → "Run workflow"
   - Choose the version bump level (patch/minor/major)

5. **Check workflow runs**:
   - Monitor the Actions tab for delivery and release workflow status
   - Review workflow logs if issues arise
