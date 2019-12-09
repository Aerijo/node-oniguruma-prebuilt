const cp = require("child_process");
const path = require("path");

function install() {
  cp.execSync("tree", {stdio: "inherit"});
  cp.execSync("autoreconf -vfi", {cwd: path.resolve(__dirname, "..", "deps", "oniguruma"), stdio: "inherit"});
  cp.execSync("./configure", {cwd: path.resolve(__dirname, "..", "deps", "oniguruma"), stdio: "inherit"});
}

install();
