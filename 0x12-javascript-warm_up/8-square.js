#!/usr/bin/node

const size = process.argv[2];
if (size === undefined) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    console.log('x'.repeat(size));
  }
}
