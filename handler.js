var fs = require('fs');

function handler(inputs) {

    console.log("Handler ..");
    var inputs = JSON.parse(inputs);
    console.log("p1:", inputs.p1);
    console.log("p2:", inputs.p2);
    console.log("filepath:", inputs.file);
    input = JSON.parse(fs.readFileSync(inputs.file, 'utf8'));
    console.debug("inputfile:", input);
}

handler(process.argv[2]);