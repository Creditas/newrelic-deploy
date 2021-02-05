# newrelic-deploy

## Install

```bash
$ pip install newrelic-deploy
```

## Create new revision

To create a new release, you need to edit the [setup.py](https://github.com/Creditas/newrelic-deploy/blob/master/setup.py#L8) file, stating the number of the new version.

After you merge, the Travis CI [pipeline](https://travis-ci.org/github/Creditas/newrelic-deploy/) will automatically publish the new version at https://pypi.org/project/newrelic-deploy/


## Using

### Running:
```bash
$ newrelic-deploy --key NEWRELIC_KEY --app APP_ID
```
