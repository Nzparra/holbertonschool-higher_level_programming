#!/usr/bin/node
exports.esrever = function (list) {
  let size = list.length - 1;
  let i = 0;
  while ((size - 1) > 0) {
    const e = list[size];
    list[size] = list[i];
    list[i] = e;
    size--;
    i++;
  }
  return list;
};
