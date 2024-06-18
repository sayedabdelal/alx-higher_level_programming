#!/usr/bin/node
// #!/usr/local/bin/node
const str1 = 'X';
const number = parseInt(process.argv[2], 10);
if (!isNaN(number) && number > 0) {
  for (let k = 0; k < number; k++) {
    let result = '';
    for (let x = 0; x < number; x++) {
        result += str1;
    }
    console.log(result);
  }
} else if (isNaN(number)) {
  console.log('Missing size');
}