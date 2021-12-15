#!/usr/bin/node
exports.nbOccurrences = function (list, searchElement) {
  let cnt = 0;

  for (const val of list) {
    if (val === searchElement) cnt += 1;
  }
  return (cnt);
};
