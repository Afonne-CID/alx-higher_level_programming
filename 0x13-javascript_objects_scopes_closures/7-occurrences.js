#!/usr/bin/node
exports.nbOccurrences = function (list, searchElement) {
  let cnt = 0;

  for (const i in list) {
    if (list[i] === searchElement) cnt++;
  }
  return (cnt);
};
