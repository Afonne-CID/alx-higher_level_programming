#!/usr/bin/node
exports.nbOccurrences = function (list, searchElement) {
  return list.reduce((count, current) => current === searchElement ? count + 1 : count, 0);
};
