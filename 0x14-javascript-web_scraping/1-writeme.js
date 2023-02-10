#!/usr/bin/node

const fs = require('fs');
const filename = process.argv[2];
const string = process.argv[3];

fs.writeFile(filename, string, 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
});
