# my.dispatch
Sandbox for dispatch testing. 

## Workflow Dispatch

- GH App requires `Action Write` scope
- API requires Token with `repo` scope
- The `Workflow` dispatch requires the workflow **file** to be in the default branch to run. 
  - Thus, requires committing a new yml to the default branch (`main`) to enable running & changing in the branch

- Examples running via GitHub CLI using `name`, or `file.yml` with extension):

  ```
  gh workflow run my-workflow -f p1=Whatever -F p2=@./specs/input.json
  gh workflow run wf.yml (same as above)
  gh workflow run myworkflow --ref the.branch
  ```

  ```
  gh run watch
  ```
  
## Repository Dispatch

- Requires toggling the default branch 
- GH App requires  `metadata:read` and `contenst:read&write`
- API requires Token with `repo` scope


## Setup

The `GH_TOKEN` environement variable is required. 

The python scripts require:
```
python -m pip install requests
```


## References

- [Manually Running a workflow](https://docs.github.com/en/actions/managing-workflow-runs/manually-running-a-workflow)
- [Create a workflow dispatch event](https://docs.github.com/en/rest/reference/actions#create-a-workflow-dispatch-event)
- [Create a repository dispatch event](https://docs.github.com/en/rest/reference/repos#create-a-repository-dispatch-event)


