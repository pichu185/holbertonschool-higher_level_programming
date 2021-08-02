#!/usr/bin/node
const arguments = process.argv[2];
if (!arguments) {
	console.log('No argument');
} else {
  console.log(arguments);
}
