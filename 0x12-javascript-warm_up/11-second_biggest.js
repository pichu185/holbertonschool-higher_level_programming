#!/usr/bin/node

const args = process.argv;
if (args.length < 4) {
  console.log(0);
} else {
  const list = [];
  for (let i = 2; args[i] !== undefined; i++) {
    list.push(parseInt(args[i]));
  }
  list.sort();
  list.pop();
  console.log(list[list.length - 1]);
}
