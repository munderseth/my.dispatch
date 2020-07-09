function handler(inputs) {

    console.log("Handler ..");
    var inputs = JSON.parse(inputs);
    console.log("p1: ", inputs.p1);
    var fileinput = JSON.parse(inputs.fileinput);
    console.log("repo obj:", fileinput.repo);
}

handler(process.argv[2]);