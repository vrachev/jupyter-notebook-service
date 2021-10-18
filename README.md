# Flask App Example + Template

hello-flask is an example app viewable at:
- https://hello-flask.internal-tools.staging.corp.mongodb.com
- https://hello-flask.internal-tools.prod.corp.mongodb.com

and can be used as a template for other Flask apps.


## Overview
This app includes
- The usage of [tox](https://tox.readthedocs.io/en/latest/) to run:
  - An automated code formatter [black](https://black.readthedocs.io/en/stable/)
  - Tests with test coverage [pytest](https://docs.pytest.org/en/latest/)
- A pipeline to deploy your app via [Kanopy](https://github.com/10gen/kanopy-docs), with:
  - An example for setting environment variables and secrets
  - An example for metrics collecting/sending
  - An example for logging to Splunk
- Use of gunicorn for staging and production environments


## Adding to the template
- Add filenames and search terms to be updated in `make_project.py`
(In other words, if you add a file to the template repo that contains "hello-flask" in it, you would add it to the list of files to searched and replaced.)


## Usage
### Using the template
The `make_project.py` script:
1) Creates a new directory with your app name in the specified parent directory.
2) Updates occurrences of `hello-flask` with your project's name in all files, and updates occurrences of python versions.

Execute the script by running `make_project.py` with command line arguments `--app-name, --parent-directory, --python-version`:
Examples:
- `./make_project.py --app-name [YOUR_APP_NAME]`
- `./make_project.py --app-name [YOUR_APP_NAME] --parent-directory [PARENT_DIRECTORY]`
- `./make_project.py --app-name [YOUR_APP_NAME] --python-version [PYTHON_VERSION]`

Example: `./make_project.py --app-name my-new-project --parent-directory ../ --python-version 3.7.6`

__Notes__:
- Usage of `--python-version` should be considered with available [Docker Official Images](https://hub.docker.com/_/python)
- `gevent` (a current dependency of the hello-flask app) is currently compatible with python versions <= 3.7


### Deploying your app
- Create a repo for your app via MANA (with team access to the repo)
- [Setup your kubectl configuration](https://github.com/10gen/kanopy-docs/blob/master/docs/kubeconfig.md)
- If applicable, [configure secret environment variables](https://github.com/10gen/kanopy-docs/blob/master/docs/application_configuration.md#configuring-secret-environment-variables) and update in appropriate environment files
- [Configure your repo in drone](https://github.com/10gen/kanopy-docs/blob/master/docs/getting_started.md#configure-repository-in-drone)
- [Configure your secrets in drone](https://github.com/10gen/kanopy-docs/blob/master/docs/getting_started.md#configure-repository-in-drone)
- Obtain the `slack_webhook` token from a team member and configure in drone with the other secrets
- [Configure your apps resource limits](https://github.com/10gen/kanopy-docs/blob/master/docs/production_checklist.md#resource-requestslimits)


### Testing your app
- Run `tox`
