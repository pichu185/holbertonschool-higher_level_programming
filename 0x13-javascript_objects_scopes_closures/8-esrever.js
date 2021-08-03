#!/usr/bin/node

exports.esrever = function (list) {
  const largo = list.length - 1;
  const listcopy = [];
  for (let j = largo; j >= 0; j--) {
    listcopy.push(list[j]);
  }
  return listcopy;
};
