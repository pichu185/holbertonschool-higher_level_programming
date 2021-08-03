#!/usr/bin/node

const list = require('./100-data').list;

const temp = list.map((element, index) => element * index);
console.log(list);
console.log(temp);
