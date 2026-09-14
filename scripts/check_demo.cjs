// Check the numerical behavior of the browser demo without a browser dependency.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const scope = vm.createContext({ document: { querySelector: () => null, querySelectorAll: () => [] } });
vm.runInContext(fs.readFileSync(path.join(__dirname, '../script.js'), 'utf8'), scope);
for (let a = -20; a <= 20; a++) for (let b = -20; b <= 20; b++) {
  const result = vm.runInContext(`forwardPass(${a/20}, ${b/20})`, scope);
  assert.ok(result.hidden.every(n => Number.isFinite(n) && n >= 0));
  assert.ok(result.probabilities.every(n => Number.isFinite(n) && n >= 0 && n <= 1));
  assert.ok(Math.abs(result.probabilities.reduce((sum, p) => sum + p, 0) - 1) < 1e-12);
}
const predict = (a, b) => JSON.stringify(vm.runInContext(`forwardPass(${a}, ${b}).probabilities`, scope));
assert.notEqual(predict(-1, 0), predict(1, 0));
assert.notEqual(predict(0, -1), predict(0, 1));
console.log('PASS: 1,681 input combinations produce valid probabilities; both inputs affect output');
