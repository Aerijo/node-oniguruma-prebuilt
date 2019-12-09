const cp = require("child_process");
const path = require("path");

function install() {
  if (process.platform === "win32") {
    // cp.execSync('"nmake.exe" --version', {cwd: path.resolve(__dirname, "..", "deps", "oniguruma"), stdio: "inherit"});
    cp.execSync("make_win.bat", {cwd: path.resolve(__dirname, "..", "deps", "oniguruma"), stdio: "inherit"});
  } else {
    cp.execSync("autoreconf -vfi", {cwd: path.resolve(__dirname, "..", "deps", "oniguruma"), stdio: "inherit"});
    cp.execSync("./configure", {cwd: path.resolve(__dirname, "..", "deps", "oniguruma"), stdio: "inherit"});
  }
}

install();
