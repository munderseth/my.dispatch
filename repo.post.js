const { Octokit } = require("@octokit/rest");

var token = process.env.GH_TOKEN;

var octokit = new Octokit({ auth: token });

octokit.request('POST /repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches', {
    owner: 'munderseth',
    repo: 'my.dispatch',
    workflow_id: 'wf.yml',
    ref: 'master'
  })