#!/usr/bin/node
const args = require('process').argv;

if (args.length >= 3) {
  const argPassed = args.slice(2, 3).toString();
  console.log(argPassed);
} else {
  console.log('No argument');
}
