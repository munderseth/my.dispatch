const { Octokit } = require("@octokit/rest");

var token = process.env.GH_TOKEN;

var octokit = new Octokit({ auth: token });

var myinput = {"p1": "one", "p2": "two"};

var myinputs = { 
 p1: "js",
}

//inputs: JSON.stringify(myinput)

octokit.request('POST /repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches', {
    owner: 'munderseth',
    repo: 'my.dispatch',
    workflow_id: 'wf.yml',
    ref: 'master',
    inputs: myinputs,
  })