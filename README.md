## My custom pre-commit hooks 

These pre-commit hooks are very basic and only meet my needs: (i.e. for testing
and my own repositories). 

It's not ready for production use. 

Check out the example folder and add the `.pre-commit-config.yaml` file to your
repository.

### List of available hooks

```
- id: generic-check-for-binary-files
- id: generic-fix-end-of-files
- id: generic-non-breaking-spaces
- id: generic-replace-tabs-with-spaces
- id: generic-trailing-whitespaces
- id: python-ruff-formatter
- id: python-ruff-linter
- id: terraform-format
```
