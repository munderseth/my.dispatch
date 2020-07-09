const { Octokit } = require("@octokit/rest");
var fs = require('fs');

var token = process.env.GH_TOKEN;

var octokit = new Octokit({ auth: token });

var myinput = {"p1": "one", "p2": "two"};
var myinputJSON = JSON.stringify(myinput);

var myinputs = { 
 p1: "js",
 fileinput: myinputJSON
}

//inputs: JSON.stringify(myinput)

octokit.request('POST /repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches', {
    owner: 'munderseth',
    repo: 'my.dispatch',
    workflow_id: 'wf.yml',
    ref: 'master',
    inputs: myinputs,
  })