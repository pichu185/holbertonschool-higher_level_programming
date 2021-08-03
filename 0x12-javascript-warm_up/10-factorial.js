#!/usr/bin/node

function factorial (x) {
  if (x === 0 || isNaN(x)) {
    return 1;
  }
  return (x * factorial(x - 1));
}
const x = parseInt(process.argv[2]);
console.log(factorial(x));
