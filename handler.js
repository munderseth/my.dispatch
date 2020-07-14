function handler(inputs) {

    console.log("Handler ..");
    var inputs = JSON.parse(inputs);
    console.log("p1: ", inputs.p1);
    console.log("fileinput: ", inputs.fileinput);
}

handler(process.argv[2]);