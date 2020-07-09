const { Octokit } = require("@octokit/rest");
var fs = require('fs');

var token = process.env.GH_TOKEN;

var octokit = new Octokit({ auth: token });

// Converting to Obj, then back to String cleans up the - \r\n and spaces
var myinputs = { 
 p1: "js",
 fileinput: JSON.stringify(JSON.parse(fs.readFileSync('test.json', 'utf8')))
}

//inputs: JSON.stringify(myinput)

octokit.request('POST /repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches', {
    owner: 'munderseth',
    repo: 'my.dispatch',
    workflow_id: 'wf.yml',
    ref: 'master',
    inputs: myinputs,
  })