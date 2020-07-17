function handler(inputs) {

    console.log("Handler ..");
    var inputs = JSON.parse(inputs);
    console.log("p1:", inputs.p1);
    console.log("p2:", inputs.p2);
    console.log("filepath:", inputs.filepath);
}

handler(process.argv[2]);