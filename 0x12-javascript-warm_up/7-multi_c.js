#!/usr/bin/node
// #!/usr/local/bin/node

const number = parseInt(process.argv[2], 10);

if (!isNaN(number)) {
    for (let k = 0; k < number; k++) {
        console.log('C is fun');
    }
} else {
    console.log('Missing number of occurrences');
}