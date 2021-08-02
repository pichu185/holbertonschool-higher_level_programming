#!/usr/bin/node

const myVar = 'C is fun';
const x = process.argv[2];
if (x === undefined) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log(myVar);
  }
}
