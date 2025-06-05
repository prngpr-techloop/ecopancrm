# Ecopan ERP

This repository contains the **Ecopan ERP** application, a comprehensive enterprise resource planning system built on the **Frappe Framework** and **ERPNext**. This application is designed to meet Ecopan's specific internal business needs, integrating core ERP functionalities with essential CRM features.

## Key Features

  * **Ecopan ERP**: Core ERP functionalities tailored for Ecopan's internal operations.
  * **Minimal CRM Capabilities**: Essential customer relationship management features integrated within the ERP for streamlined operations.
  * **Document Management**: A complete solution for archiving, searching, and managing internal company documents.

-----

## Installation

To install the Ecopan ERP application in your Frappe/ERPNext environment, follow these steps using the `bench` CLI:

```bash
cd $PATH_TO_YOUR_BENCH # Navigate to your bench directory
bench get-app https://github.com/your-repo-url/ecopancrm.git --branch develop # Replace with the actual URL of your repository
bench install-app ecopancrm
```

**Note**: Make sure to replace `https://github.com/your-repo-url/ecopancrm.git` with the actual URL of your repository.

-----

## Code Quality

This application uses **pre-commit** to automate code formatting and linting, ensuring consistent code quality across the project.

### Pre-commit Setup

1.  **Install pre-commit**: If you haven't already, install `pre-commit` by following the official instructions.

2.  **Enable Hooks**: Navigate to the app directory and enable the pre-commit hooks:

    ```bash
    cd apps/ecopancrm
    pre-commit install
    ```

### Formatting and Linting Tools

`pre-commit` is configured to use the following tools for checking and formatting your code:

  * **ruff**: An extremely fast Python linter and formatter.
  * **eslint**: A JavaScript linter.
  * **prettier**: An opinionated code formatter.
  * **pyupgrade**: Upgrades Python syntax to newer versions.

-----

## Continuous Integration (CI)

This project leverages **GitHub Actions** for continuous integration, ensuring code stability and quality. The following workflows are configured:

  * **CI**: Installs this app and runs unit tests on every push to the `develop` branch.
  * **Linters**: Runs **Frappe Semgrep Rules** and **pip-audit** on every pull request to identify potential security vulnerabilities and code issues.

-----
