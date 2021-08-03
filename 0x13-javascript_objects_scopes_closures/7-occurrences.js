#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let x = 0;
  list.forEach(element => {
    if (element === searchElement) {
      x++;
    }
  });
  return x;
};
